# Mistral OCR Tool & Skill

A powerful, standalone Python tool (packaged as an OpenClaw Skill) to convert PDF documents into Markdown with extracted images, powered by Mistral AI's OCR API.

## 🌟 Features

- **High-Quality OCR**: Leverages `mistral-ocr-latest` model for accurate text recognition.
- **Image Extraction**: Automatically extracts images from PDFs and saves them locally.
- **Markdown Output**: Generates a clean Markdown file with correct image references.
- **Standalone Usage**: Can be used as a CLI tool in any Python environment.
- **Skill Ready**: Pre-packaged structure for AI Agent frameworks (like OpenClaw).

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- [uv](https://github.com/astral-sh/uv) (Recommended for dependency management) or pip.
- A Mistral AI API Key from [console.mistral.ai](https://console.mistral.ai/).

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sldyns/mistral-ocr-skill.git
   cd mistral-ocr-skill
   ```

2. Install dependencies:
   ```bash
   # Using pip
   pip install mistralai
   
   # Or using uv (recommended)
   uv venv
   uv pip install mistralai
   ```

## 💻 Usage

### As a CLI Tool (Standalone)

You can run the script directly from the command line without any agent framework.

```bash
# Set your API key
export MISTRAL_API_KEY="your_api_key_here"

# Run the processor
python skills/mistral-ocr/ocr_processor.py \
  --pdf_path "/path/to/your/document.pdf" \
  --api_key "$MISTRAL_API_KEY"
```

**Output**:
The script will create a folder named after your PDF file containing:
- `document_name.md`: The converted markdown content.
- `image_x_y.png`: Extracted images referenced in the markdown.

### As an AI Agent Skill (e.g., OpenClaw)

This repository follows the standard Agent Skill structure.

1. **Install**: Clone this repo into your agent's skill directory (e.g., `~/.openclaw/workspace/skills/`).
2. **Configure**: Add your `MISTRAL_API_KEY` to your agent's configuration (e.g., `openclaw.json`).
3. **Invoke**: The agent can now use the `mistral-ocr` tool to read PDFs.

## 📂 Project Structure

```text
.
├── README.md           # This file
└── skills
    └── mistral-ocr
        ├── SKILL.md          # Agent Skill Definition (Metadata & Instructions)
        └── ocr_processor.py  # Core Logic Script
```

## 🛠️ How It Works

1. **Upload**: The script uploads your PDF to Mistral's temporary storage.
2. **Process**: It requests OCR processing using the `mistral-ocr-latest` model.
3. **Extract**: It parses the JSON response to find base64-encoded images and text blocks.
4. **Reconstruct**: It saves images to disk and reconstructs the document layout in Markdown format.

## License

MIT
