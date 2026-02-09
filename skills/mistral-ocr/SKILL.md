---
name: mistral-ocr
description: Convert PDF to Markdown with images using Mistral OCR.
homepage: https://mistral.ai/
metadata:
  {
    "openclaw":
      {
        "emoji": "📄",
        "requires": { "bins": ["uv"], "env": ["MISTRAL_API_KEY"] },
        "primaryEnv": "MISTRAL_API_KEY",
        "install":
          [
            {
              "id": "uv-brew",
              "kind": "brew",
              "formula": "uv",
              "bins": ["uv"],
              "label": "Install uv (brew)",
            },
          ],
      },
  }
---

# Mistral OCR

Convert PDF documents to Markdown, extracting text and images.

Usage:

```bash
uv run --with mistralai {baseDir}/ocr_processor.py --pdf_path "/path/to/document.pdf" --api_key "$MISTRAL_API_KEY"
```

Configuration:

- `MISTRAL_API_KEY`: Set this environment variable or configure it in `~/.openclaw/openclaw.json` under `skills."mistral-ocr".env.MISTRAL_API_KEY`.

Output:

The script returns a JSON object with the path to the generated Markdown file and extracted images.

---

# Mistral OCR (中文说明)

使用 Mistral OCR 将 PDF 文档转换为 Markdown 格式，并提取文本和图片。

使用方法：

```bash
uv run --with mistralai {baseDir}/ocr_processor.py --pdf_path "/path/to/document.pdf" --api_key "$MISTRAL_API_KEY"
```

配置说明：

- `MISTRAL_API_KEY`：设置此环境变量，或在 `~/.openclaw/openclaw.json` 中的 `skills."mistral-ocr".env.MISTRAL_API_KEY` 下进行配置。

输出结果：

脚本返回一个 JSON 对象，包含生成的 Markdown 文件路径和提取的图片信息。
