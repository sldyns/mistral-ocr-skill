# Mistral OCR Skill

This skill allows OpenClaw to convert PDF documents into Markdown with extracted images using the Mistral OCR API.

## Overview

- **Name**: `mistral-ocr`
- **Description**: Convert PDF to Markdown with images using Mistral OCR.
- **Author**: sldyns (Kun Qian)
- **Repository**: https://github.com/sldyns/mistral-ocr-skill

## Prerequisite

- **Mistral API Key**: Get one from [Mistral AI Console](https://console.mistral.ai/).
- **Python Environment**: Requires `uv` for dependency management.

## Configuration

Set your API key in `~/.openclaw/openclaw.json`:

```json
{
  "skills": {
    "mistral-ocr": {
      "apiKey": "YOUR_MISTRAL_API_KEY"
    }
  }
}
```

Or use the environment variable `MISTRAL_API_KEY`.

## Usage

### Convert a PDF

```bash
uv run --with mistralai {baseDir}/ocr_processor.py --pdf_path "/path/to/document.pdf" --api_key "$MISTRAL_API_KEY"
```

The script will:
1. Upload the PDF to Mistral.
2. Process it using the `mistral-ocr-latest` model.
3. Extract images and save them locally.
4. Generate a Markdown file with correct image references.
5. Return a JSON object with the result paths.

### Output Structure

The output will be saved in a directory named after the PDF file (sanitized).

```text
/path/to/document_folder/
  ├── document_name.md       # The generated Markdown
  ├── image_1_1.png          # Extracted images
  └── image_1_2.png
```

## Troubleshooting

- **API Key Error**: Ensure `MISTRAL_API_KEY` is set correctly.
- **File Access**: Ensure the PDF path is absolute and readable.
- **Network**: Check your internet connection to Mistral API.
