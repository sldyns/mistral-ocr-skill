# Mistral OCR Skill

This repository contains the `mistral-ocr` skill for OpenClaw. It allows you to convert PDF documents to Markdown with extracted images using Mistral's OCR API.

## Installation

You can install this skill using the `clawhub` CLI or manually.

### Manual Installation

1. Clone this repository into your OpenClaw skills directory (e.g., `~/.openclaw/workspace/skills/`).
2. Ensure you have `uv` installed.
3. Configure your `MISTRAL_API_KEY` in `~/.openclaw/openclaw.json`.

## Skill Structure

- `skills/mistral-ocr/SKILL.md`: The skill definition file.
- `skills/mistral-ocr/ocr_processor.py`: The Python script that interacts with the Mistral API.

## Usage

See `skills/mistral-ocr/SKILL.md` for detailed usage instructions.

---

# Mistral OCR Skill (中文说明)

本仓库包含 OpenClaw 的 `mistral-ocr` 技能。它允许您使用 Mistral 的 OCR API 将 PDF 文档转换为带有提取图像的 Markdown 格式。

## 安装

您可以使用 `clawhub` CLI 或手动安装此技能。

### 手动安装

1. 将此仓库克隆到您的 OpenClaw 技能目录（例如 `~/.openclaw/workspace/skills/`）。
2. 确保已安装 `uv`。
3. 在 `~/.openclaw/openclaw.json` 中配置您的 `MISTRAL_API_KEY`。

## 技能结构

- `skills/mistral-ocr/SKILL.md`：技能定义文件。
- `skills/mistral-ocr/ocr_processor.py`：与 Mistral API 交互的 Python 脚本。

## 使用方法

详细的使用说明请参阅 `skills/mistral-ocr/SKILL.md`。
