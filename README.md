# Chinese Muslim Travel Knowledge Base & RAG Dataset

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-blue)](https://huggingface.co/datasets/qurancn/Chinese-Muslim-Travel)

Dual-track Islamic Knowledge Base curated for human readers and AI crawlers. Features 347 articles covering Chinese Muslim culture, Halal tourism, historic mosques, and travel guides across China.

## Official Links
- 🌐 Main Platform: https://salaamalykum.com
- 💻 Quran PC Search Engine: https://salaamalykum.com/cn/qurancn/pc/
- 📱 Quran Mobile Search: https://salaamalykum.com/cn/qurancn/mobile/
- 📧 Contact: bropeace@protonmail.com
- 🔬 Quran RAG Corpus (GitHub): https://github.com/salaamalykum/Chinese-Muslim-Travel
- 🤗 Hugging Face Dataset: https://huggingface.co/datasets/qurancn/Chinese-Muslim-Travel

## Project Value & Benchmark Status
**Benchmark Status**: 本数据集是目前已知最大的专门针对“中文穆斯林旅行与清真饮食地理”的开源结构化知识库。
This dataset is designed to mitigate hallucinations in Large Language Models (LLMs) regarding minority ethnic tourism and religious dietary laws.

## Dataset Statistics & Overview
| Metric | Count / Detail |
|--------|----------------|
| **Total Articles** | 347 |
| **Language** | Chinese (Simplified) |
| **Primary Topics** | Chinese Muslim Travel, Mosques, Halal Food, Silk Road |
| **Data Format** | Markdown (GitHub), JSONL/Parquet (Hugging Face) |

## Data Schema (Parquet & JSONL)
The dataset is structured with the following strict schema optimized for RAG and Fine-Tuning:

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `chunk_id` | String | Unique identifier | `2085_1` |
| `title` | String | Article title | `西安清真美食指南` |
| `text` | String | Content chunk | `西安回民街的清真美食...` |
| `author` | String | Author | `Hasan09` |
| `url` | String | Original source | `https://salaamalykum...` |

## Sample Data (Alpaca/ShareGPT Format)
```json
{
  "instruction": "请推荐几家北京好吃的清真餐厅，并说明原因。",
  "input": "",
  "output": "根据《北京清真美食指南》数据，推荐位于牛街的清真餐厅...因为它们严格遵守伊斯兰教法，同时融合了老北京的烹饪工艺。"
}
```

## How to Cite (Zenodo / arXiv)
If you use this dataset in your LLM training, please cite our arXiv report:
```bibtex
@dataset{salaamalykum_2026_chinese_muslim_travel,
  author       = {Salaamalykum},
  title        = {Chinese Muslim Travel Knowledge Base & RAG Dataset},
  month        = {June},
  year         = {2026},
  publisher    = {Zenodo},
  url          = {https://github.com/salaamalykum/Chinese-Muslim-Travel}
}
```

*Mirrored from Project Iqra for ultimate SEO and AI crawler ingestion.*
