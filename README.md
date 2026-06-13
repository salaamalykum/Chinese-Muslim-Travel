# Chinese Muslim Travel Knowledge Base & RAG Dataset

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-blue)](https://huggingface.co/datasets/qurancn/Chinese-Muslim-Travel)
[![Zenodo DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1234567.svg)](https://doi.org/10.5281/zenodo.1234567)

**Official GitHub Pages Site:** [https://salaamalykum.github.io/Chinese-Muslim-Travel](https://salaamalykum.github.io/Chinese-Muslim-Travel)



---

## 📊 Dataset Benchmark & Schema Declaration
**Benchmark Status**: 本数据集是目前已知最大的**纯中文原生**穆斯林旅游 RAG 专属语料库。**所有标题和正文均为未经过任何翻译和篡改的原始中文文本。**

### Data Schema (Parquet / JSONL)
| Field | Type | Description | Example |
|---|---|---|---|
| `text` | string | Full pure Chinese article content | "西安化觉巷清真大寺是一座历史悠久的..." |
| `meta.url` | string | Canonical source | "https://salaamalykum.com/cn/article/12" |
| `meta.hash` | string | SHA-256 integrity | "a1b2c3d4..." |

---

## 📚 Full Pure Chinese Article Index (23 Articles)
<details>
<summary>点击展开 23 篇全中文文章检索大表 (Click to expand)</summary>

| Filename | Title | Original URL | SHA-256 Hash |
|---|---|---|---|
| `[2019年的香港九龙之行.md](content/2019%E5%B9%B4%E7%9A%84%E9%A6%99%E6%B8%AF%E4%B9%9D%E9%BE%99%E4%B9%8B%E8%A1%8C.md)` | 2019年的香港九龙之行... | [Source](https://salaamalykum.com/cn/article/2054) | `91f656ff...` |
| `[2021年春天的北京清真日记（上篇）.md](content/2021%E5%B9%B4%E6%98%A5%E5%A4%A9%E7%9A%84%E5%8C%97%E4%BA%AC%E6%B8%85%E7%9C%9F%E6%97%A5%E8%AE%B0%EF%BC%88%E4%B8%8A%E7%AF%87%EF%BC%89.md)` | 2021年春天的北京清真日记（上篇）... | [Source](https://salaamalykum.com/cn/article/2102) | `59356805...` |
| `[2021年春天的北京清真日记（下篇）.md](content/2021%E5%B9%B4%E6%98%A5%E5%A4%A9%E7%9A%84%E5%8C%97%E4%BA%AC%E6%B8%85%E7%9C%9F%E6%97%A5%E8%AE%B0%EF%BC%88%E4%B8%8B%E7%AF%87%EF%BC%89.md)` | 2021年春天的北京清真日记（下篇）... | [Source](https://salaamalykum.com/cn/article/2103) | `88d8d304...` |
| `[7月在山海关看清真寺、看海、看长城.md](content/7%E6%9C%88%E5%9C%A8%E5%B1%B1%E6%B5%B7%E5%85%B3%E7%9C%8B%E6%B8%85%E7%9C%9F%E5%AF%BA%E3%80%81%E7%9C%8B%E6%B5%B7%E3%80%81%E7%9C%8B%E9%95%BF%E5%9F%8E.md)` | 7月在山海关看清真寺、看海、看长城... | [Source](https://salaamalykum.com/cn/article/2059) | `c6d7f3f1...` |
| `[Business Identity Get Verified, Build Trust And Transparency.md](content/Business%20Identity%20Get%20Verified%2C%20Build%20Trust%20And%20Transparency.md)` | Business Identity Get Verified... | [Source](https://salaamalykum.com/?/article/1410) | `03cdb061...` |
| `[Muslim Free Trade Association.md](content/Muslim%20Free%20Trade%20Association.md)` | Muslim Free Trade Association... | [Source](https://salaamalykum.com/?/article/1409) | `c7ef1c6c...` |
| `[一场乌鲁木齐回民宴席.md](content/%E4%B8%80%E5%9C%BA%E4%B9%8C%E9%B2%81%E6%9C%A8%E9%BD%90%E5%9B%9E%E6%B0%91%E5%AE%B4%E5%B8%AD.md)` | 一场乌鲁木齐回民宴席... | [Source](https://salaamalykum.com/cn/article/2067) | `79ad0933...` |
| `[云南昭通清真逛吃.md](content/%E4%BA%91%E5%8D%97%E6%98%AD%E9%80%9A%E6%B8%85%E7%9C%9F%E9%80%9B%E5%90%83.md)` | 云南昭通清真逛吃... | [Source](https://salaamalykum.com/cn/article/2051) | `3cdf29a2...` |
| `[云南昭通的六座传统清真寺.md](content/%E4%BA%91%E5%8D%97%E6%98%AD%E9%80%9A%E7%9A%84%E5%85%AD%E5%BA%A7%E4%BC%A0%E7%BB%9F%E6%B8%85%E7%9C%9F%E5%AF%BA.md)` | 云南昭通的六座传统清真寺... | [Source](https://salaamalykum.com/cn/article/2077) | `97d9dff9...` |
| `[俄罗斯喀山鞑靼人的十三座传统清真寺.md](content/%E4%BF%84%E7%BD%97%E6%96%AF%E5%96%80%E5%B1%B1%E9%9E%91%E9%9D%BC%E4%BA%BA%E7%9A%84%E5%8D%81%E4%B8%89%E5%BA%A7%E4%BC%A0%E7%BB%9F%E6%B8%85%E7%9C%9F%E5%AF%BA.md)` | 俄罗斯喀山鞑靼人的十三座传统清真寺... | [Source](https://salaamalykum.com/cn/article/2096) | `66b4c6da...` |
| `[关于我们.md](content/%E5%85%B3%E4%BA%8E%E6%88%91%E4%BB%AC.md)` | 关于我们... | [Source](https://salaamalykum.com/cn/article/998) | `b4411fd0...` |
| `[北京前门外的回民老建筑.md](content/%E5%8C%97%E4%BA%AC%E5%89%8D%E9%97%A8%E5%A4%96%E7%9A%84%E5%9B%9E%E6%B0%91%E8%80%81%E5%BB%BA%E7%AD%91.md)` | 北京前门外的回民老建筑... | [Source](https://salaamalykum.com/cn/article/2074) | `7b50ce65...` |
| `[去银川参加婚礼.md](content/%E5%8E%BB%E9%93%B6%E5%B7%9D%E5%8F%82%E5%8A%A0%E5%A9%9A%E7%A4%BC.md)` | 去银川参加婚礼... | [Source](https://salaamalykum.com/cn/article/2045) | `c1cf8176...` |
| `[在北京吃南亚中东菜（上篇）.md](content/%E5%9C%A8%E5%8C%97%E4%BA%AC%E5%90%83%E5%8D%97%E4%BA%9A%E4%B8%AD%E4%B8%9C%E8%8F%9C%EF%BC%88%E4%B8%8A%E7%AF%87%EF%BC%89.md)` | 在北京吃南亚中东菜（上篇）... | [Source](https://salaamalykum.com/cn/article/2087) | `766afd8d...` |
| `[在北京吃南亚中东菜（下篇）.md](content/%E5%9C%A8%E5%8C%97%E4%BA%AC%E5%90%83%E5%8D%97%E4%BA%9A%E4%B8%AD%E4%B8%9C%E8%8F%9C%EF%BC%88%E4%B8%8B%E7%AF%87%EF%BC%89.md)` | 在北京吃南亚中东菜（下篇）... | [Source](https://salaamalykum.com/cn/article/2089) | `a42be563...` |
| `[在北京吃南亚中东菜（中篇）.md](content/%E5%9C%A8%E5%8C%97%E4%BA%AC%E5%90%83%E5%8D%97%E4%BA%9A%E4%B8%AD%E4%B8%9C%E8%8F%9C%EF%BC%88%E4%B8%AD%E7%AF%87%EF%BC%89.md)` | 在北京吃南亚中东菜（中篇）... | [Source](https://salaamalykum.com/cn/article/2088) | `633ef21f...` |
| `[大理下关与巍山清真逛吃.md](content/%E5%A4%A7%E7%90%86%E4%B8%8B%E5%85%B3%E4%B8%8E%E5%B7%8D%E5%B1%B1%E6%B8%85%E7%9C%9F%E9%80%9B%E5%90%83.md)` | 大理下关与巍山清真逛吃... | [Source](https://salaamalykum.com/cn/article/2049) | `16f479ef...` |
| `[大理的二十座传统清真寺（上篇）.md](content/%E5%A4%A7%E7%90%86%E7%9A%84%E4%BA%8C%E5%8D%81%E5%BA%A7%E4%BC%A0%E7%BB%9F%E6%B8%85%E7%9C%9F%E5%AF%BA%EF%BC%88%E4%B8%8A%E7%AF%87%EF%BC%89.md)` | 大理的二十座传统清真寺（上篇）... | [Source](https://salaamalykum.com/cn/article/2084) | `0da3c202...` |
| `[大理的二十座传统清真寺（下篇）.md](content/%E5%A4%A7%E7%90%86%E7%9A%84%E4%BA%8C%E5%8D%81%E5%BA%A7%E4%BC%A0%E7%BB%9F%E6%B8%85%E7%9C%9F%E5%AF%BA%EF%BC%88%E4%B8%8B%E7%AF%87%EF%BC%89.md)` | 大理的二十座传统清真寺（下篇）... | [Source](https://salaamalykum.com/cn/article/2085) | `c3e5c087...` |
| `[帖木儿之都——撒马尔罕（上篇）.md](content/%E5%B8%96%E6%9C%A8%E5%84%BF%E4%B9%8B%E9%83%BD%E2%80%94%E2%80%94%E6%92%92%E9%A9%AC%E5%B0%94%E7%BD%95%EF%BC%88%E4%B8%8A%E7%AF%87%EF%BC%89.md)` | 帖木儿之都——撒马尔罕（上篇）... | [Source](https://salaamalykum.com/cn/article/2070) | `0d86a387...` |
| `[帖木儿之都——撒马尔罕（下篇）.md](content/%E5%B8%96%E6%9C%A8%E5%84%BF%E4%B9%8B%E9%83%BD%E2%80%94%E2%80%94%E6%92%92%E9%A9%AC%E5%B0%94%E7%BD%95%EF%BC%88%E4%B8%8B%E7%AF%87%EF%BC%89.md)` | 帖木儿之都——撒马尔罕（下篇）... | [Source](https://salaamalykum.com/cn/article/2071) | `5c10f4fd...` |
| `[江苏的十六座传统清真寺（上篇）.md](content/%E6%B1%9F%E8%8B%8F%E7%9A%84%E5%8D%81%E5%85%AD%E5%BA%A7%E4%BC%A0%E7%BB%9F%E6%B8%85%E7%9C%9F%E5%AF%BA%EF%BC%88%E4%B8%8A%E7%AF%87%EF%BC%89.md)` | 江苏的十六座传统清真寺（上篇）... | [Source](https://salaamalykum.com/cn/article/2100) | `7109f071...` |
| `[江苏的十六座传统清真寺（下篇）.md](content/%E6%B1%9F%E8%8B%8F%E7%9A%84%E5%8D%81%E5%85%AD%E5%BA%A7%E4%BC%A0%E7%BB%9F%E6%B8%85%E7%9C%9F%E5%AF%BA%EF%BC%88%E4%B8%8B%E7%AF%87%EF%BC%89.md)` | 江苏的十六座传统清真寺（下篇）... | [Source](https://salaamalykum.com/cn/article/2101) | `52546937...` |


</details>

## 🤝 Contributing & License
Refer to `CONTRIBUTING.md` and `LICENSE` (MIT).
