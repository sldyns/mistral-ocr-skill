import os
import sys
import json
import base64
import re
import uuid
import traceback
from pathlib import Path
import argparse
from mistralai import Mistral
from mistralai import DocumentURLChunk, ImageURLChunk, TextChunk
from mistralai.models import OCRResponse

# 强制设置stdout编码为UTF-8
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        # Python 3.6不支持reconfigure
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() == 'pdf'

def extract_images_from_ocr(ocr_response, output_dir):
    """Extract images from OCR response and save to directory"""
    image_paths = {}
    
    for page_idx, page in enumerate(ocr_response.pages):
        for img_idx, img in enumerate(page.images):
            # Generate image filename
            img_filename = f"image_{page_idx+1}_{img_idx+1}.png"
            img_path = os.path.join(output_dir, img_filename)
            
            # Decode and save image
            img_data = base64.b64decode(img.image_base64.split(',')[1] if ',' in img.image_base64 else img.image_base64)
            with open(img_path, 'wb') as f:
                f.write(img_data)
            
            # Record image ID and path
            image_paths[img.id] = img_filename
    
    return image_paths

def process_markdown(markdown_text, image_paths, relative_path=""):
    """Replace image references in markdown with local paths"""
    for img_id, img_path in image_paths.items():
        # Replace image reference format ![image_id](image_id) with ![image_id](relative_path/image_path)
        markdown_text = markdown_text.replace(
            f"![{img_id}]({img_id})", 
            f"![{img_id}]({os.path.join(relative_path, img_path)})"
        )
    return markdown_text

def process_ocr(pdf_path, api_key):
    """Process OCR for PDF file"""
    try:
        # Check if file exists
        if not os.path.exists(pdf_path):
            return {"error": f"File does not exist: {pdf_path}"}
        
        # Check file type
        if not allowed_file(pdf_path):
            return {"error": "Only PDF files are supported"}
        
        # Create Mistral client
        client = Mistral(api_key=api_key)
        
        # Get original filename (without extension)
        filename_base = os.path.splitext(os.path.basename(pdf_path))[0]
        
        # Create safe filename
        safe_filename = re.sub(r'[^\w\s-]', '', filename_base).strip().lower()
        safe_filename = re.sub(r'[-\s]+', '-', safe_filename)
        
        # If filename is empty, use random ID
        if not safe_filename:
            safe_filename = str(uuid.uuid4())
        
        # Create result directory
        parent_dir = os.path.dirname(pdf_path)
        result_dir = os.path.join(parent_dir, safe_filename)
        os.makedirs(result_dir, exist_ok=True)
        
        log_info(f"Processing file: {pdf_path}")
        log_info(f"Save directory: {result_dir}")
        
        # Upload PDF file
        uploaded_file = client.files.upload(
            file={
                "file_name": os.path.basename(pdf_path),
                "content": Path(pdf_path).read_bytes(),
            },
            purpose="ocr",
        )
        
        log_info(f"File uploaded successfully, ID: {uploaded_file.id}")
        
        # Get signed URL
        signed_url = client.files.get_signed_url(file_id=uploaded_file.id, expiry=1)
        
        log_info("Signed URL obtained, processing OCR...")
        
        # Process OCR
        ocr_response = client.ocr.process(
            document=DocumentURLChunk(document_url=signed_url.url), 
            model="mistral-ocr-latest", 
            include_image_base64=True
        )
        
        log_info("OCR processing complete, extracting images...")
        
        # Extract images and save
        image_paths = extract_images_from_ocr(ocr_response, result_dir)
        
        log_info(f"Extracted {len(image_paths)} images, processing Markdown...")
        
        # Process and save markdown
        all_markdown = []
        for page_idx, page in enumerate(ocr_response.pages):
            # Process single page markdown, replace image paths
            processed_markdown = process_markdown(page.markdown, image_paths)
            all_markdown.append(processed_markdown)
        
        # Combine all pages markdown
        combined_markdown = "\n\n".join(all_markdown)
        
        # Save markdown file
        markdown_path = os.path.join(result_dir, f"{safe_filename}.md")
        with open(markdown_path, 'w', encoding='utf-8') as f:
            f.write(combined_markdown)
        
        log_info(f"Markdown saved successfully: {markdown_path}")
        
        # Return success result
        return {
            "success": True,
            "message": "OCR processing successful",
            "result_path": result_dir,
            "markdown_file": os.path.join(result_dir, f"{safe_filename}.md"),
            "image_count": len(image_paths)
        }
        
    except Exception as e:
        error_msg = str(e)
        log_error(f"Error during processing: {error_msg}")
        log_error(traceback.format_exc())
        return {"error": f"Error during processing: {error_msg}"}

def log_info(message):
    """Log info message"""
    print(f"[INFO] {message}")

def log_error(message):
    """Log error message"""
    print(f"[ERROR] {message}", file=sys.stderr)

def main():
    """Main function"""
    parser = argparse.ArgumentParser(description='Process OCR for PDF file')
    parser.add_argument('--pdf_path', required=True, help='PDF file path')
    parser.add_argument('--api_key', required=False, help='Mistral AI API Key', default=os.environ.get('MISTRAL_API_KEY'))
    
    args = parser.parse_args()
    
    if not args.api_key:
        print("[ERROR] API key is required. Provide via --api_key or MISTRAL_API_KEY env var.", file=sys.stderr)
        sys.exit(1)
    
    # Process OCR
    result = process_ocr(args.pdf_path, args.api_key)
    
    # Output result as JSON
    print("\n===RESULT_JSON_BEGIN===")
    print(json.dumps(result, ensure_ascii=False))
    print("===RESULT_JSON_END===")

if __name__ == "__main__":
    main()
