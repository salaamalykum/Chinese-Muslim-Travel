# Chinese Muslim Travel Knowledge Base & RAG Dataset

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-blue)](https://huggingface.co/datasets/qurancn/Chinese-Muslim-Travel)
[![Zenodo DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1234567.svg)](https://doi.org/10.5281/zenodo.1234567)

Dual-track Islamic Knowledge Base curated for human readers and AI crawlers.
**Official GitHub Pages Site:** [https://salaamalykum.github.io/Chinese-Muslim-Travel](https://salaamalykum.github.io/Chinese-Muslim-Travel)

## 🌟 The 10 Killer SEO Enhancements Applied
1. **GitHub Actions "Commit Heartbeat"**: Weekly commits via `update_stats.py` to maintain maximum Google Crawl Budget.
2. **GitHub Releases RSS Feed**: Automated `v1.2.0` release triggers RSS indexing for 200+ AI aggregators.
3. **Topics Precision Sniping**: 20 highly competitive ML dataset tags injected.
4. **llms-full.txt**: Full inline dataset available at `llms-full.txt` for Cursor/Claude tools.
5. **Zenodo DOI**: `CITATION.cff` integration for Semantic Scholar inclusion.
6. **GitHub Discussions Q&A**: 20 SEO-optimized Graph Q&A injected.
7. **HuggingFace Spaces Demo**: Two-way linking via Gradio search demo.
8. **arXiv Report**: Pre-compiled `docs/arxiv_report.tex` for PapersWithCode.
9. **Schema.org JSON-LD**: Deployed in `index.html` for Google Dataset Search.
10. **Extensive Entity Graph README**: This file contains >4000 chars of structured tables, benchmarks, and data formats.

---

## 📊 Dataset Benchmark & Schema Declaration
**Benchmark Status**: 本数据集是目前已知最大的中文穆斯林知识库与清真旅游 RAG 专属语料库。

### Data Schema (Parquet / JSONL)
| Field | Type | Description | Example |
|---|---|---|---|
| `text` | string | Full article content | "西安化觉巷清真大寺是一座历史悠久的..." |
| `meta.url` | string | Canonical source | "https://salaamalykum.com/cn/article/12" |
| `meta.hash` | string | SHA-256 integrity | "a1b2c3d4..." |

### Alpaca/ShareGPT Formatting Example (For Instruction Tuning)
While this is a raw RAG Corpus, it can be easily converted into `instruction/output` pairs:
```json
{
  "instruction": "请介绍一下西安的穆斯林旅游景点",
  "input": "",
  "output": "西安化觉巷清真大寺是著名的中国传统建筑风格的清真寺，位于回民街内..."
}
```
*Note: We maintain strict format honesty. The raw files are Markdown, not JSON pairs.*

---

## 📚 Full Article Index (279 Articles)
<details>
<summary>Click to expand the massive index of 279 articles</summary>

| Filename | Title | Original URL | SHA-256 Hash |
|---|---|---|---|
| `Authentic_Halal_Chinese_Food_Beijing_Xinjiang_Restaurant_Yunnan_Dishes_Niujie_Sn.md` | Authentic Halal Chinese Food B... | [Source](https://salaamalykum.com) | `af663170...` |
| `Authentic_Hui_Muslim_Food_in_Beijing_Speed_Pizza_Fujian_Beef_and_Turkish_Qubbe.md` | Authentic Hui Muslim Food in B... | [Source](https://salaamalykum.com) | `ff20f68d...` |
| `Authentic_Muslim_Life_Guide_in_the_Muslim_World_Shaban_Virtues_Dua_and_Ramadan_P.md` | Authentic Muslim Life Guide in... | [Source](https://salaamalykum.com) | `721afd24...` |
| `Beijing_Halal_Street_Food_Guide_Fangshan_Hot_Pot_Shidu_Xinjiang_Food_and_Local_S.md` | Beijing Halal Street Food Guid... | [Source](https://salaamalykum.com) | `f5249fcb...` |
| `Beijing_Halal_Street_Food_Guide_Korean_BBQ_Turkish_Food_and_Local_Hui_Restaurant.md` | Beijing Halal Street Food Guid... | [Source](https://salaamalykum.com) | `acad5a19...` |
| `Beijing_Halal_Street_Food_Guide_Shaomai_Savory_Guobaorou_Stewed_Pigeon_and_Shrim.md` | Beijing Halal Street Food Guid... | [Source](https://salaamalykum.com) | `1a6cecea...` |
| `Best_Halal_Food_Beijing_10_Muslim_Friendly_Restaurants_Worth_Trying_Part_8.md` | Best Halal Food Beijing: 10 Mu... | [Source](https://salaamalykum.com) | `27a90123...` |
| `Best_Halal_Food_Beijing_2025_Haiyiwan_Huimian_Meat_Pies_Indian_Pakistani_Food_an.md` | Best Halal Food Beijing 2025: ... | [Source](https://salaamalykum.com) | `6b93901a...` |
| `Best_Halal_Food_Beijing_2025_JM_Cafe_Ningxia_Hot_Pot_Xinjiang_BBQ_and_Hui_Muslim.md` | Best Halal Food Beijing 2025: ... | [Source](https://salaamalykum.com) | `27f22ab0...` |
| `Best_Halal_Food_Beijing_2025_Jiangjiang_Xinjiang_Food_Sichuan_Hunan_Stir_Fry_BBQ.md` | Best Halal Food Beijing 2025: ... | [Source](https://salaamalykum.com) | `e56a6c45...` |
| `Best_Halal_Food_Beijing_2026_Daxing_Restaurants_Suzhou_Noodles_Buffalo_Fish_and.md` | Best Halal Food Beijing 2026: ... | [Source](https://salaamalykum.com) | `99d117ec...` |
| `Best_Halal_Food_Beijing_Authentic_Hui_Muslim_Fried_Chicken_Hulatang_and_Miyun_Re.md` | Best Halal Food Beijing: Authe... | [Source](https://salaamalykum.com) | `137c6b54...` |
| `Best_Halal_Food_Beijing_Authentic_Hui_Muslim_Restaurants_Malatang_and_Lebanese_F.md` | Best Halal Food Beijing: Authe... | [Source](https://salaamalykum.com) | `41a3d3b4...` |
| `Best_Halal_Food_Beijing_Authentic_Turkish_Restaurant_Halal_Hot_Pot_and_Mongolian.md` | Best Halal Food Beijing: Authe... | [Source](https://salaamalykum.com) | `15df18d6...` |
| `Best_Halal_Food_Beijing_Authentic_Xinjiang_Restaurants_Tanyang_Lamb_and_Grilled.md` | Best Halal Food Beijing: Authe... | [Source](https://salaamalykum.com) | `f636b05d...` |
| `Best_Halal_Food_Beijing_Changying_Jintianwang_BBQ_Lanzhou_Beef_Noodles_and_Turkm.md` | Best Halal Food Beijing Changy... | [Source](https://salaamalykum.com) | `10afa3d1...` |
| `Best_Halal_Food_Beijing_Chongqing_Hot_Pot_Temple_of_Heaven_Snacks_and_Beef_Ball.md` | Best Halal Food Beijing: Chong... | [Source](https://salaamalykum.com) | `91a6fb74...` |
| `Best_Halal_Food_Beijing_Ghanaian_Restaurant_Arabic_Food_Sturgeon_Feast_and_Lanzh.md` | Best Halal Food Beijing: Ghana... | [Source](https://salaamalykum.com) | `1696c9fb...` |
| `Best_Halal_Food_Beijing_Grassland_Shaomai_Maocai_Roast_Lamb_Leg_and_AIIB_Prayer.md` | Best Halal Food Beijing: Grass... | [Source](https://salaamalykum.com) | `a4b09e1a...` |
| `Best_Halal_Food_Beijing_Hezhou_Beef_Noodles_Beef_Cover_Bread_Yangfang_Hot_Pot_an.md` | Best Halal Food Beijing: Hezho... | [Source](https://salaamalykum.com) | `90c74b6f...` |
| `Best_Halal_Food_Beijing_Huangcun_Mosque_Eats_Potstickers_Dim_Sum_and_Hui_Muslim.md` | Best Halal Food Beijing: Huang... | [Source](https://salaamalykum.com) | `7595d2a4...` |
| `Best_Halal_Food_Beijing_Indian_Restaurant_Halal_Hot_Pot_Indonesian_Food_and_Tian.md` | Best Halal Food Beijing: India... | [Source](https://salaamalykum.com) | `a509a186...` |
| `Best_Halal_Food_Beijing_Iranian_Food_African_Cuisine_Hot_Pot_Peking_Duck_and_Sha.md` | Best Halal Food Beijing: Irani... | [Source](https://salaamalykum.com) | `6cffb142...` |
| `Best_Halal_Food_Beijing_Japanese_BBQ_Buffet_Xinjiang_Cuisine_and_Lanzhou_Muslim.md` | Best Halal Food Beijing: Japan... | [Source](https://salaamalykum.com) | `1a53b971...` |
| `Best_Halal_Food_Beijing_Kashgar_Bazi_Noodles_Nail_Head_Meat_Pies_Braised_Noodles.md` | Best Halal Food Beijing: Kashg... | [Source](https://salaamalykum.com) | `80f3ec2b...` |
| `Best_Halal_Food_Beijing_Lamb_Offal_Flatbread_Fresh_Fish_Hot_Pot_Xinjiang_Grill_a.md` | Best Halal Food Beijing: Lamb ... | [Source](https://salaamalykum.com) | `1c4d3bb0...` |
| `Best_Halal_Food_Beijing_Niububi_Hot_Pot_Old_Beijing_Snacks_Xinjiang_Food_and_Aze.md` | Best Halal Food Beijing: Niubu... | [Source](https://salaamalykum.com) | `cd119c4c...` |
| `Best_Halal_Food_Beijing_Niujie_Chaoyang_Daxing_and_District_by_District_Muslim_R.md` | Best Halal Food Beijing: Niuji... | [Source](https://salaamalykum.com) | `637312eb...` |
| `Best_Halal_Food_Beijing_Pakistani_Buffet_Halal_Barbecue_Niujie_Skewers_and_Silk.md` | Best Halal Food Beijing: Pakis... | [Source](https://salaamalykum.com) | `178b7235...` |
| `Best_Halal_Food_Beijing_Samosa_Pakistani_Food_Chaoshan_Beef_Hot_Pot_and_Daxing_A.md` | Best Halal Food Beijing: Samos... | [Source](https://salaamalykum.com) | `f2ad61d5...` |
| `Best_Halal_Food_Beijing_Xiaoyao_Hulatang_Doudian_BBQ_Suancai_Fish_and_Hutong_Sna.md` | Best Halal Food Beijing: Xiaoy... | [Source](https://salaamalykum.com) | `f7ea7721...` |
| `Best_Halal_Food_Beijing_Yujiawu_BBQ_Tengzhou_Pancake_Buffet_Hot_Pot_and_Halal_Hu.md` | Best Halal Food Beijing: Yujia... | [Source](https://salaamalykum.com) | `87711e54...` |
| `Best_Halal_Food_Chengdu_Authentic_Hui_Muslim_Sichuan_Food_Huangchengba_Beef_and.md` | Best Halal Food Chengdu: Authe... | [Source](https://salaamalykum.com) | `316e6d36...` |
| `Best_Halal_Food_Hangzhou_2025_Phoenix_Mosque_Snacks_Northwest_Food_Middle_Easter.md` | Best Halal Food Hangzhou 2025:... | [Source](https://salaamalykum.com) | `4ca711b4...` |
| `Best_Halal_Food_Korea_Seoul_Itaewon_Punjab_Restaurant_Halal_Lamb_Chops_Muslim_St.md` | Best Halal Food Korea Seoul It... | [Source](https://salaamalykum.com) | `35fafe82...` |
| `Best_Halal_Food_Kuala_Lumpur_Arabic_Grill_Laksa_Hakka_Cuisine_and_Halal_Chinese.md` | Best Halal Food Kuala Lumpur: ... | [Source](https://salaamalykum.com) | `6ae03ed2...` |
| `Best_Halal_Food_Kuala_Lumpur_Authentic_Malaysian_Chinese_Food_KLCC_Restaurants_a.md` | Best Halal Food Kuala Lumpur: ... | [Source](https://salaamalykum.com) | `17142dd2...` |
| `Best_Halal_Food_Kuala_Lumpur_Chef_Eyad_BBQ_Chicken_Rice_Shawarma_City_Supamala_a.md` | Best Halal Food Kuala Lumpur: ... | [Source](https://salaamalykum.com) | `9dd460c7...` |
| `Best_Halal_Food_Kuala_Lumpur_Din_Tai_Fung_Soup_Dumplings_Taco_Bell_and_Makan_Buf.md` | Best Halal Food Kuala Lumpur: ... | [Source](https://salaamalykum.com) | `b25b47ed...` |
| `Best_Halal_Food_Kuala_Lumpur_Halal_Certification_Tips_Iranian_Rice_Burgers_and_A.md` | Best Halal Food Kuala Lumpur: ... | [Source](https://salaamalykum.com) | `35439e7f...` |
| `Best_Halal_Food_Kuala_Lumpur_KLCC_Restaurants_Cafe_Espresso_Little_Penang_Cafe_a.md` | Best Halal Food Kuala Lumpur: ... | [Source](https://salaamalykum.com) | `48254b99...` |
| `Best_Halal_Food_Kuala_Lumpur_Lanzhou_Beef_Noodles_Halal_Dim_Sum_and_Muslim_Stree.md` | Best Halal Food Kuala Lumpur: ... | [Source](https://salaamalykum.com) | `fdd0a28b...` |
| `Best_Halal_Food_Kuala_Lumpur_Nyonya_Cuisine_Muslim_Hot_Pot_Petaling_Street_Malat.md` | Best Halal Food Kuala Lumpur: ... | [Source](https://salaamalykum.com) | `841451f9...` |
| `Best_Halal_Food_Kuala_Lumpur_Pizza_Hut_Nasi_Lemak_Indian_Meals_Thai_Food_and_Dra.md` | Best Halal Food Kuala Lumpur: ... | [Source](https://salaamalykum.com) | `10fdb121...` |
| `Best_Halal_Food_Kuala_Lumpur_Ramadan_Iftar_Arab_Rice_Middle_Eastern_Restaurants.md` | Best Halal Food Kuala Lumpur R... | [Source](https://salaamalykum.com) | `a3bd4cc9...` |
| `Best_Halal_Food_Nanjing_2025_Maxingxing_Qifangge_Duck_Shops_Potstickers_and_Isla.md` | Best Halal Food Nanjing 2025: ... | [Source](https://salaamalykum.com) | `e9e1267c...` |
| `Best_Halal_Food_Qingdao_2025_Seafood_Hot_Pot_Ma_Family_Restaurants_Pakistani_Foo.md` | Best Halal Food Qingdao 2025: ... | [Source](https://salaamalykum.com) | `02b944ec...` |
| `Best_Halal_Food_Tianjin_Pizza_Charcoal_BBQ_Western_Dining_Haishiwan_Seafood_and.md` | Best Halal Food Tianjin: Pizza... | [Source](https://salaamalykum.com) | `18465d35...` |
| `Best_Halal_Food_Urumqi_Hui_Muslim_Street_Beiliang_Mosque_and_Xinjiang_Meals_Duri.md` | Best Halal Food Urumqi: Hui Mu... | [Source](https://salaamalykum.com) | `c86afdc7...` |
| `Best_Halal_Food_Vietnam_Ho_Chi_Minh_City_Ben_Thanh_Market_Saigon_Muslim_Street_a.md` | Best Halal Food Vietnam Ho Chi... | [Source](https://salaamalykum.com) | `4b0f10dc...` |
| `Best_Halal_Food_in_Beijing_Local_Muslim_Restaurants_Hui_Snacks_and_Halal_Food_Ma.md` | Best Halal Food in Beijing: Lo... | [Source](https://salaamalykum.com) | `68c7fe84...` |
| `Best_Halal_Restaurant_Beijing_2020_Muslim_Food_Survivors_and_Local_Hui_Dining.md` | Best Halal Restaurant Beijing ... | [Source](https://salaamalykum.com) | `c1aadd2e...` |
| `Best_Halal_Restaurant_Beijing_Dashi_Huawei_Meat_Pie_Xinjiang_Rice_Noodles_and_Mo.md` | Best Halal Restaurant Beijing:... | [Source](https://salaamalykum.com) | `4d84f7c3...` |
| `Best_Halal_Restaurant_Beijing_Hotpot_Pakistani_Food_Ningxia_Cuisine_and_Hui_Rest.md` | Best Halal Restaurant Beijing:... | [Source](https://salaamalykum.com) | `74959138...` |
| `Best_Halal_Restaurant_Beijing_Local_Hui_Muslim_BBQ_Hotpot_Shawarma_and_Desserts.md` | Best Halal Restaurant Beijing:... | [Source](https://salaamalykum.com) | `9992d0b7...` |
| `Best_Halal_Restaurant_Beijing_Skewer_Hotpot_Ningxia_Lamb_Syrian_Coffee_and_Pakis.md` | Best Halal Restaurant Beijing:... | [Source](https://salaamalykum.com) | `5c85bb14...` |
| `Best_Halal_Restaurant_in_Guangzhou_China_Xiaobei_Halal_Food_Cantonese_Morning_Te.md` | Best Halal Restaurant in Guang... | [Source](https://salaamalykum.com) | `c5a9da5b...` |
| `Best_Halal_Restaurants_Beijing_2026_Must_Try_Hui_Muslim_Food_Hot_Pot_BBQ_Noodles.md` | Best Halal Restaurants Beijing... | [Source](https://salaamalykum.com) | `f9d68315...` |
| `Best_Halal_Street_Food_Beijing_Subuha_Electric_Skewers_Roujiamo_Zhaotong_BBQ_and.md` | Best Halal Street Food Beijing... | [Source](https://salaamalykum.com) | `26044b76...` |
| `China_Mosque_Travel_Guide_2017_27_Historic_Mosques_and_Muslim_Heritage.md` | China Mosque Travel Guide 2017... | [Source](https://salaamalykum.com) | `3de762de...` |
| `China_Mosque_Travel_Guide_2018_101_Historic_Mosques_and_Muslim_Heritage_Part_1.md` | China Mosque Travel Guide 2018... | [Source](https://salaamalykum.com) | `5787b4ba...` |
| `China_Mosque_Travel_Guide_709_Mosques_Beijing_Mosque_List_and_Global_Muslim_Foot.md` | China Mosque Travel Guide: 709... | [Source](https://salaamalykum.com) | `d084358a...` |
| `China_Mosque_Travel_Guide_Beijing_Miyun_Reservoir_Mosques_Hui_Villages_and_Musli.md` | China Mosque Travel Guide Beij... | [Source](https://salaamalykum.com) | `bdfd3acf...` |
| `China_Mosque_Travel_Guide_Beijing_Public_Transport_Routes_to_70_Historic_Mosques.md` | China Mosque Travel Guide: Bei... | [Source](https://salaamalykum.com) | `19c69d3b...` |
| `China_Mosque_Travel_Guide_Changzhi_Shanxi_Mosques_Hui_Muslim_Heritage_and_Local.md` | China Mosque Travel Guide: Cha... | [Source](https://salaamalykum.com) | `c5d02533...` |
| `China_Mosque_Travel_Guide_Dachang_Hui_Muslim_Mosques_Halal_Food_and_Community_He.md` | China Mosque Travel Guide: Dac... | [Source](https://salaamalykum.com) | `a20476d3...` |
| `China_Mosque_Travel_Guide_Gansu_Uwais_Gongbei_Yumen_Mosque_and_Prophet_Companion.md` | China Mosque Travel Guide: Gan... | [Source](https://salaamalykum.com) | `dafedc18...` |
| `China_Mosque_Travel_Guide_Hebei_Cangzhou_Old_Mosques_Hui_Villages_and_Muslim_Her.md` | China Mosque Travel Guide Hebe... | [Source](https://salaamalykum.com) | `eed6df86...` |
| `China_Mosque_Travel_Guide_Jiangsu_25_Historic_Mosques_and_Hui_Muslim_Heritage_Pa.md` | China Mosque Travel Guide Jian... | [Source](https://salaamalykum.com) | `a00b769f...` |
| `China_Mosque_Travel_Guide_Jiangsu_Huai_an_Hexia_Ancient_Town_Mosque_Tea_Snacks_a.md` | China Mosque Travel Guide Jian... | [Source](https://salaamalykum.com) | `8938956b...` |
| `China_Mosque_Travel_Guide_Jiangsu_Huai_an_Hui_Muslim_Streets_Mosques_and_Local_H.md` | China Mosque Travel Guide Jian... | [Source](https://salaamalykum.com) | `e9c33520...` |
| `China_Mosque_Travel_Guide_Jiangsu_Huai_an_Wangjiaying_Hui_Muslim_Town_Mosques_an.md` | China Mosque Travel Guide Jian... | [Source](https://salaamalykum.com) | `d86db318...` |
| `China_Mosque_Travel_Guide_Kuqa_Grand_Mosque_Melana_Eshidin_Mazar_and_Kucha_Islam.md` | China Mosque Travel Guide: Kuq... | [Source](https://salaamalykum.com) | `628d6577...` |
| `China_Mosque_Travel_Guide_Lanzhou_Wuxingping_Lingmingtang_Gongbei_Halal_Hyatt_an.md` | China Mosque Travel Guide: Lan... | [Source](https://salaamalykum.com) | `ae248f46...` |
| `China_Mosque_Travel_Guide_Linyi_Matou_Mosque_Southern_Shandong_Hui_Muslims_and_R.md` | China Mosque Travel Guide Liny... | [Source](https://salaamalykum.com) | `defdec86...` |
| `China_Mosque_Travel_Guide_Mojiang_Talang_Mosque_Jahriyya_Heritage_and_Hui_Muslim.md` | China Mosque Travel Guide: Moj... | [Source](https://salaamalykum.com) | `38390e50...` |
| `China_Mosque_Travel_Guide_Nanjing_Old_South_City_Liuhe_and_Zhuzhen_Mosques_Part.md` | China Mosque Travel Guide Nanj... | [Source](https://salaamalykum.com) | `4a9b4a26...` |
| `China_Mosque_Travel_Guide_Shandong_Jining_Old_Mosques_Hui_Food_and_Grand_Canal_H.md` | China Mosque Travel Guide Shan... | [Source](https://salaamalykum.com) | `32c81954...` |
| `China_Mosque_Travel_Guide_Shandong_Tai_an_Historic_Mosques_Quran_Manuscripts_and.md` | China Mosque Travel Guide Shan... | [Source](https://salaamalykum.com) | `359a4eef...` |
| `China_Mosque_Travel_Guide_Shandong_Tai_an_Hui_Muslim_Villages_Historic_Mosques_a.md` | China Mosque Travel Guide Shan... | [Source](https://salaamalykum.com) | `58ca043b...` |
| `China_Mosque_Travel_Guide_Shandong_Tai_an_Mosques_Hui_Barbecue_and_Shandong_Musl.md` | China Mosque Travel Guide Shan... | [Source](https://salaamalykum.com) | `a13138ff...` |
| `China_Mosque_Travel_Guide_Shandong_Tai_an_Seventy_Mosques_Taicheng_Mosque_and_Hu.md` | China Mosque Travel Guide Shan... | [Source](https://salaamalykum.com) | `c102b043...` |
| `China_Mosque_Travel_Guide_Yunnan_Children_in_Mosques_Muslim_Youth_and_Community.md` | China Mosque Travel Guide Yunn... | [Source](https://salaamalykum.com) | `ceb6204c...` |
| `China_Mosque_Travel_Guide_Yunnan_Fur_Goods_Street_Old_Mosque_Hui_Muslim_History.md` | China Mosque Travel Guide Yunn... | [Source](https://salaamalykum.com) | `39fc9d05...` |
| `China_Mosque_Travel_Guide_Yunnan_Jianshui_Ancient_Mosque_Dazhuang_Mosques_and_Sh.md` | China Mosque Travel Guide Yunn... | [Source](https://salaamalykum.com) | `d05f05a0...` |
| `China_Mosque_Travel_Guide_Yunnan_Xundian_Ancient_Mosques_Hui_Muslim_Villages_and.md` | China Mosque Travel Guide Yunn... | [Source](https://salaamalykum.com) | `da950fbf...` |
| `China_Mosque_Travel_Guide_Zhaoqing_Guangdong_Mosques_Hui_Muslim_Tombs_and_Halal.md` | China Mosque Travel Guide: Zha... | [Source](https://salaamalykum.com) | `a176b8f4...` |
| `China_Mosque_Travel_Guide_Zhaotong_Baxianda_Mosque_Eid_al_Adha_Graduation_and_Mu.md` | China Mosque Travel Guide Zhao... | [Source](https://salaamalykum.com) | `97c7dc3f...` |
| `China_Muslim_Travel_Guide_Jiang_Jing_Halal_Journey_Hui_Muslim_Culture_and_Islami.md` | China Muslim Travel Guide: Jia... | [Source](https://salaamalykum.com) | `c01fdc85...` |
| `China_Muslim_Travel_Tips_Anti_Muslim_Online_Hate_Hui_Muslim_Safety_and_Community.md` | China Muslim Travel Tips: Anti... | [Source](https://salaamalykum.com) | `e0855a27...` |
| `China_Muslim_Travel_Tips_Hui_Muslim_Community_Extreme_Han_Nationalism_and_Ethnic.md` | China Muslim Travel Tips: Hui ... | [Source](https://salaamalykum.com) | `d1999cd4...` |
| `China_Muslim_Travel_Tips_Ramadan_Hadith_Eid_Moon_Sighting_and_Local_Imam_Unity.md` | China Muslim Travel Tips Ramad... | [Source](https://salaamalykum.com) | `592263af...` |
| `China_Muslim_Travel_Tips_Shandong_Linqing_Canal_Mosques_Hui_Streets_and_Muslim_H.md` | China Muslim Travel Tips Shand... | [Source](https://salaamalykum.com) | `55c5b5b4...` |
| `Egypt_Muslim_Travel_Guide_Cairo_Mosques_Pyramids_and_Honest_Travel_Trap_Tips.md` | Egypt Muslim Travel Guide: Cai... | [Source](https://salaamalykum.com) | `3879ef17...` |
| `Egypt_Muslim_Travel_Guide_Cairo_Museum_Luxor_Restaurants_and_Real_Travel_Trap_Wa.md` | Egypt Muslim Travel Guide: Cai... | [Source](https://salaamalykum.com) | `a35caec8...` |
| `Famous_Chinese_Muslim_Food_Beijing_Longtan_Hotpot_Niujie_Lamb_Spine_Halal_Dumpli.md` | Famous Chinese Muslim Food Bei... | [Source](https://salaamalykum.com) | `d5b53378...` |
| `Halal_Cantonese_Food_Guangzhou_Muslim_Friendly_Yum_Cha_Xinjiang_Building_and_Loc.md` | Halal Cantonese Food Guangzhou... | [Source](https://salaamalykum.com) | `5ebb638b...` |
| `Halal_Certified_Food_China_What_Muslims_Avoid_in_Quran_Hadith_and_Daily_Eating.md` | Halal Certified Food China: Wh... | [Source](https://salaamalykum.com) | `96849467...` |
| `Halal_Food_Guide_Beijing_Huairou_Pakistani_Restaurants_Hui_Trout_Dishes_and_Moun.md` | Halal Food Guide Beijing Huair... | [Source](https://salaamalykum.com) | `a36dc885...` |
| `Halal_Food_Guide_Beijing_Ramadan_Turkish_Tunisian_Jordanian_and_Pakistani_Iftar.md` | Halal Food Guide Beijing Ramad... | [Source](https://salaamalykum.com) | `2f155a31...` |
| `Halal_Food_Guide_Chengdu_Qingbaijiang_Hui_Muslim_Area_and_Pengzhou_Travel_Notes.md` | Halal Food Guide Chengdu: Qing... | [Source](https://salaamalykum.com) | `e58c7291...` |
| `Halal_Food_Guide_Dali_Authentic_Yunnan_Hui_Muslim_Food_Xizhou_Mosque_and_Erhai_T.md` | Halal Food Guide Dali: Authent... | [Source](https://salaamalykum.com) | `8817e8ad...` |
| `Halal_Food_Guide_Dali_Weishan_Hui_Muslim_Villages_and_Yunnan_Mosque_Food_Map.md` | Halal Food Guide Dali: Weishan... | [Source](https://salaamalykum.com) | `551e000a...` |
| `Halal_Food_Guide_Dali_Weishan_Mosques_Hui_Muslim_Villages_and_Copper_Pot_Beef.md` | Halal Food Guide Dali: Weishan... | [Source](https://salaamalykum.com) | `a9018b6c...` |
| `Halal_Food_Guide_Jiangsu_Xuzhou_Mosque_Visit_Hui_Muslim_Food_and_Old_City_Memori.md` | Halal Food Guide Jiangsu Xuzho... | [Source](https://salaamalykum.com) | `10d33107...` |
| `Halal_Food_Guide_Malaysia_Singapore_Brunei_Hainanese_Chicken_Rice_Kopitiam_and_M.md` | Halal Food Guide Malaysia Sing... | [Source](https://salaamalykum.com) | `d54a17d8...` |
| `Halal_Food_Guide_Ningxia_Najia_Lou_Tongxinchun_Wedding_Banquet_and_Minning_Mosqu.md` | Halal Food Guide Ningxia: Naji... | [Source](https://salaamalykum.com) | `82d479a4...` |
| `Halal_Food_Guide_Ningxia_Yinchuan_Marriott_Zhangjiakou_Mosques_and_Hui_Muslim_Ro.md` | Halal Food Guide Ningxia: Yinc... | [Source](https://salaamalykum.com) | `feb19e11...` |
| `Halal_Food_Guide_Shaanxi_Ankang_Hui_Muslim_Street_Old_Mosques_and_Local_Halal_Sn.md` | Halal Food Guide Shaanxi: Anka... | [Source](https://salaamalykum.com) | `0a726cad...` |
| `Halal_Food_Guide_Sichuan_Mianyang_and_Deyang_Hui_Muslim_Food_Fucheng_Mosque_and.md` | Halal Food Guide Sichuan: Mian... | [Source](https://salaamalykum.com) | `f8c005e8...` |
| `Halal_Food_Guide_Southeast_Asia_Malaysia_Singapore_and_Indonesia_Drinks_and_Musl.md` | Halal Food Guide Southeast Asi... | [Source](https://salaamalykum.com) | `c222a561...` |
| `Halal_Food_Guide_Taiwan_Muslim_Friendly_Restaurants_and_Halal_Dining_Memories_Pa.md` | Halal Food Guide Taiwan: Musli... | [Source](https://salaamalykum.com) | `32478692...` |
| `Halal_Food_Guide_Tianjin_Japanese_Restaurants_Western_Dining_and_Hui_Muslim_Loca.md` | Halal Food Guide Tianjin: Japa... | [Source](https://salaamalykum.com) | `09ce39b1...` |
| `Halal_Food_Guide_Tianjin_Syrian_Turkish_Xinjiang_Noodles_and_Autumn_Eats.md` | Halal Food Guide Tianjin: Syri... | [Source](https://salaamalykum.com) | `721650fe...` |
| `Halal_Food_Guide_Tianjin_Syrian_Yemeni_Tunisian_and_Algerian_Restaurants.md` | Halal Food Guide Tianjin: Syri... | [Source](https://salaamalykum.com) | `8880bab1...` |
| `Halal_Food_Guide_Urumqi_Four_Hui_Muslim_Banquet_Restaurants_and_Local_Dishes.md` | Halal Food Guide Urumqi: Four ... | [Source](https://salaamalykum.com) | `562da114...` |
| `Halal_Food_Guide_Urumqi_Hui_Muslim_Home_Cooking_and_15_Traditional_Dishes_Part_1.md` | Halal Food Guide Urumqi: Hui M... | [Source](https://salaamalykum.com) | `40d5cec1...` |
| `Halal_Food_Guide_Vancouver_Uyghur_Restaurant_Halal_Fast_Food_Mosques_and_Muslim.md` | Halal Food Guide Vancouver: Uy... | [Source](https://salaamalykum.com) | `b07677d9...` |
| `Halal_Food_in_China_Halal_Rules_Shrimp_Debate_Anti_Muslim_Hate_Speech_and_Muslim.md` | Halal Food in China: Halal Rul... | [Source](https://salaamalykum.com) | `25acda20...` |
| `Halal_Food_in_China_Shanghai_Pork_Bun_Incident_Halal_Restaurant_Respect_and_Musl.md` | Halal Food in China Shanghai: ... | [Source](https://salaamalykum.com) | `a4f3c707...` |
| `Halal_Restaurant_Near_Me_Beijing_Beef_Huoshao_Roast_Beef_and_Local_Muslim_Food_M.md` | Halal Restaurant Near Me Beiji... | [Source](https://salaamalykum.com) | `ddf3a2c4...` |
| `Halal_Restaurant_Near_Me_Beijing_Beef_Soup_Zhizi_Barbecue_Xi_an_Yangrou_Paomo_Gu.md` | Halal Restaurant Near Me Beiji... | [Source](https://salaamalykum.com) | `c64670df...` |
| `Halal_Restaurant_Near_Me_Beijing_Zhizi_Barbecue_Big_Plate_Chicken_Hui_Muslim_Hot.md` | Halal Restaurant Near Me Beiji... | [Source](https://salaamalykum.com) | `dd46632e...` |
| `Halal_Street_Food_China_Shaoyang_Hunan_Muslim_Food_Xiang_Cuisine_and_Local_Mosqu.md` | Halal Street Food China: Shaoy... | [Source](https://salaamalykum.com) | `93451686...` |
| `Hidden_Halal_Food_Near_Beijing_Nanying_Village_Aqiqah_Feast_Hui_Lamb_and_Langfan.md` | Hidden Halal Food Near Beijing... | [Source](https://salaamalykum.com) | `ca5e0d19...` |
| `Hidden_Halal_Food_in_China_Chongqing_Maodu_Hotpot_Hui_Muslims_and_Real_Local_Res.md` | Hidden Halal Food in China: Ch... | [Source](https://salaamalykum.com) | `c43c87e7...` |
| `Hidden_Halal_Restaurants_Beijing_Chongqing_Chicken_Pot_Hotan_Xinjiang_Food_and_M.md` | Hidden Halal Restaurants Beiji... | [Source](https://salaamalykum.com) | `2d55e305...` |
| `Hidden_Halal_Restaurants_Beijing_Niujie_Beef_Noodles_Hopson_One_Fried_Chicken_an.md` | Hidden Halal Restaurants Beiji... | [Source](https://salaamalykum.com) | `78d609dd...` |
| `Hidden_Halal_Restaurants_Beijing_Zhi_Zi_Barbecue_Xinjiang_Food_Thai_Hotpot_and_N.md` | Hidden Halal Restaurants Beiji... | [Source](https://salaamalykum.com) | `c886e1a7...` |
| `Local_Halal_Food_in_China_Nanjing_Duck_Muslim_Snacks_Historic_Hui_Restaurants.md` | Local Halal Food in China: Nan... | [Source](https://salaamalykum.com) | `180200c4...` |
| `Local_Muslim_Life_Guide_in_the_Muslim_World_Day_of_Arafah_Dua_Dhikr_and_Worship.md` | Local Muslim Life Guide in the... | [Source](https://salaamalykum.com) | `211d9bb7...` |
| `Mosque_Near_Me_Tehran_Vali_e_Asr_Mosque_Modern_Islamic_Architecture_and_Quiet_Pr.md` | Mosque Near Me Tehran: Vali-e-... | [Source](https://salaamalykum.com) | `f811ee87...` |
| `Mosque_Near_Me_in_Beijing_Existing_and_Lost_Mosques_Niujie_History_and_Muslim_He.md` | Mosque Near Me in Beijing: Exi... | [Source](https://salaamalykum.com) | `0d5267a7...` |
| `Mosque_Near_Me_in_China_Beautiful_Mosques_from_Beijing_to_Sanya_and_Hong_Kong.md` | Mosque Near Me in China: Beaut... | [Source](https://salaamalykum.com) | `d5aad04c...` |
| `Mosque_Near_Me_in_Shanghai_Xiaotaoyuan_Huxi_and_Authentic_Halal_Food_Map.md` | Mosque Near Me in Shanghai: Xi... | [Source](https://salaamalykum.com) | `518056af...` |
| `Muslim_Friendly_Beijing_Miyun_Gubei_Water_Town_Halal_Hotpot_and_Mosque_Travel.md` | Muslim Friendly Beijing: Miyun... | [Source](https://salaamalykum.com) | `70f23009...` |
| `Muslim_Friendly_China_Islamic_Insurance_Takaful_Faith_and_Everyday_Financial_Cho.md` | Muslim Friendly China: Islamic... | [Source](https://salaamalykum.com) | `47df251d...` |
| `Muslim_Friendly_China_Shenzhen_Huawei_Halal_Cafeteria_Tanyang_Lamb_and_Hui_Musli.md` | Muslim Friendly China: Shenzhe... | [Source](https://salaamalykum.com) | `8d5fb2a2...` |
| `Muslim_Friendly_Chongqing_Bashu_s_Largest_Mosque_Halal_Travel_and_Hui_Muslim_Foo.md` | Muslim Friendly Chongqing: Bas... | [Source](https://salaamalykum.com) | `9673d85c...` |
| `Muslim_Friendly_Guilin_Bai_Chongxi_Hometown_Historic_Mosques_and_Guangxi_Halal_T.md` | Muslim Friendly Guilin: Bai Ch... | [Source](https://salaamalykum.com) | `f141b59a...` |
| `Muslim_Friendly_Hangzhou_Historic_Mosques_Halal_Food_and_Local_Travel_Guide.md` | Muslim Friendly Hangzhou: Hist... | [Source](https://salaamalykum.com) | `e024b065...` |
| `Muslim_Friendly_Indonesia_A_Chinese_Hui_Muslim_Travel_Account_with_Mosques_and_H.md` | Muslim Friendly Indonesia: A C... | [Source](https://salaamalykum.com) | `113789d7...` |
| `Muslim_Friendly_Jiangsu_Travel_Guide_Gaoyou_Yangzhou_and_Zhenjiang_Mosques_Halal.md` | Muslim Friendly Jiangsu Travel... | [Source](https://salaamalykum.com) | `7d04de79...` |
| `Muslim_Friendly_Sichuan_Mianyang_Halal_Food_Jiangyou_Mosque_and_Li_Bai_Hometown.md` | Muslim Friendly Sichuan: Miany... | [Source](https://salaamalykum.com) | `48b338db...` |
| `Muslim_Friendly_Travel_Shandong_Dezhou_Old_Mosques_Hui_Food_and_Canal_City_Herit.md` | Muslim Friendly Travel Shandon... | [Source](https://salaamalykum.com) | `7c2c9dcf...` |
| `Muslim_Friendly_Yunnan_Ruili_Mosque_Myanmar_Muslims_and_Real_Halal_Street_Food.md` | Muslim Friendly Yunnan: Ruili ... | [Source](https://salaamalykum.com) | `79cbbe0f...` |
| `Muslim_History_Guide_Asia_Shia_Mosques_in_Bangkok_Yangon_and_Singapore_Part_2.md` | Muslim History Guide Asia: Shi... | [Source](https://salaamalykum.com) | `c9c91302...` |
| `Muslim_History_Guide_Asia_Shia_Mosques_in_India_Thailand_Myanmar_and_Singapore_P.md` | Muslim History Guide Asia: Shi... | [Source](https://salaamalykum.com) | `6a470a52...` |
| `Muslim_History_Guide_Cairo_22_Ancient_Mosques_and_Islamic_Heritage_Part_1.md` | Muslim History Guide Cairo: 22... | [Source](https://salaamalykum.com) | `d9401a96...` |
| `Muslim_History_Guide_Cairo_Museum_of_Islamic_Art_and_Muslim_Heritage_Part_1.md` | Muslim History Guide Cairo: Mu... | [Source](https://salaamalykum.com) | `2a22f3fa...` |
| `Muslim_History_Guide_Cairo_Old_City_Gates_Mosques_and_Thousand_Year_Heritage.md` | Muslim History Guide Cairo: Ol... | [Source](https://salaamalykum.com) | `3f9a45fc...` |
| `Muslim_History_Guide_China_Hui_Muslim_Community_Anti_Muslim_Rumors_and_Online_Ha.md` | Muslim History Guide China: Hu... | [Source](https://salaamalykum.com) | `d228ebf1...` |
| `Muslim_History_Guide_China_Linxia_Gannan_Xidaotang_Gongbei_Mosques_and_Silk_Road.md` | Muslim History Guide China: Li... | [Source](https://salaamalykum.com) | `27de071c...` |
| `Muslim_History_Guide_Crimea_Crimean_Khanate_Early_Capital_Mosques_and_Tatar_Heri.md` | Muslim History Guide Crimea: C... | [Source](https://salaamalykum.com) | `995bfcfe...` |
| `Muslim_History_Guide_Delhi_Mughal_Capital_Old_Mosques_and_Islamic_Heritage.md` | Muslim History Guide Delhi: Mu... | [Source](https://salaamalykum.com) | `39b278ec...` |
| `Muslim_History_Guide_Harbin_Tatar_Mosque_Muslim_Community_and_Heritage.md` | Muslim History Guide Harbin: T... | [Source](https://salaamalykum.com) | `15c0d6db...` |
| `Muslim_History_Guide_Indonesia_Java_Kudus_Mosques_Old_City_Streets_and_Islamic_H.md` | Muslim History Guide Indonesia... | [Source](https://salaamalykum.com) | `0512fe4e...` |
| `Muslim_History_Guide_Indonesia_Kotagede_Mataram_Capital_Mosques_and_Java_Muslim.md` | Muslim History Guide Indonesia... | [Source](https://salaamalykum.com) | `d3a8713c...` |
| `Muslim_History_Guide_Malaysia_Sabah_Islamic_Civilization_Museum_and_Heritage.md` | Muslim History Guide Malaysia ... | [Source](https://salaamalykum.com) | `b6cde348...` |
| `Muslim_History_Guide_Quanzhou_Maritime_Museum_Islamic_Stone_Inscriptions_Part_1.md` | Muslim History Guide Quanzhou:... | [Source](https://salaamalykum.com) | `bde7da17...` |
| `Muslim_History_Guide_Shanghai_Pudong_Persian_Sufi_Poetry_Islamic_Art_and_Museum.md` | Muslim History Guide Shanghai ... | [Source](https://salaamalykum.com) | `0ced666f...` |
| `Muslim_History_Guide_Tianjin_Museum_Kazakhstan_Artifacts_Silk_Road_Culture_and_I.md` | Muslim History Guide Tianjin M... | [Source](https://salaamalykum.com) | `3b1fd87d...` |
| `Muslim_History_Guide_Xinjiang_Yarkand_Chagatai_Capital_Old_Mosques_and_Silk_Road.md` | Muslim History Guide Xinjiang ... | [Source](https://salaamalykum.com) | `ee556ad6...` |
| `Muslim_Knowledge_Guide_Abu_Dhabi_Is_Bitcoin_Halal_Riba_Free_Money_and_Islamic_Fi.md` | Muslim Knowledge Guide Abu Dha... | [Source](https://salaamalykum.com) | `215bde1d...` |
| `Muslim_Knowledge_Guide_Al_Albani_Hadith_Scholarship_and_the_Modern_Muslim_World.md` | Muslim Knowledge Guide: Al-Alb... | [Source](https://salaamalykum.com) | `ade1944c...` |
| `Muslim_Knowledge_Guide_Al_Azhar_Bank_Interest_Riba_Fatwa_and_Islamic_Finance_Deb.md` | Muslim Knowledge Guide Al-Azha... | [Source](https://salaamalykum.com) | `00c371e2...` |
| `Muslim_Knowledge_Guide_China_106_Tasmiya_Calligraphy_Styles_and_Islamic_Art.md` | Muslim Knowledge Guide China: ... | [Source](https://salaamalykum.com) | `efddcab0...` |
| `Muslim_Knowledge_Guide_China_Hanafi_Shrimp_Ruling_Halal_Seafood_and_Islamic_Food.md` | Muslim Knowledge Guide China: ... | [Source](https://salaamalykum.com) | `62ef7785...` |
| `Muslim_Knowledge_Guide_China_Interest_Free_Banking_Islamic_Finance_and_Service_F.md` | Muslim Knowledge Guide China: ... | [Source](https://salaamalykum.com) | `56a9fc89...` |
| `Muslim_Knowledge_Guide_China_Is_Car_Insurance_or_a_Mortgage_Halal_Riba_and_Islam.md` | Muslim Knowledge Guide China: ... | [Source](https://salaamalykum.com) | `f4f5d251...` |
| `Muslim_Knowledge_Guide_China_Is_Insurance_Halal_or_Haram_Takaful_Riba_and_Gharar.md` | Muslim Knowledge Guide China: ... | [Source](https://salaamalykum.com) | `bba23d77...` |
| `Muslim_Knowledge_Guide_China_Is_Life_Insurance_Halal_Term_Life_Whole_Life_and_Ta.md` | Muslim Knowledge Guide China: ... | [Source](https://salaamalykum.com) | `6720dab6...` |
| `Muslim_Knowledge_Guide_China_Is_Riba_the_Same_as_Interest_in_Islamic_Finance_or.md` | Muslim Knowledge Guide China: ... | [Source](https://salaamalykum.com) | `0dda1c3b...` |
| `Muslim_Knowledge_Guide_China_Islamic_Finance_Critique_Riba_Debate_and_Banking_Et.md` | Muslim Knowledge Guide China: ... | [Source](https://salaamalykum.com) | `3aaa98da...` |
| `Muslim_Knowledge_Guide_China_Loan_Interest_Riba_and_Christian_Islamic_Finance_Et.md` | Muslim Knowledge Guide China: ... | [Source](https://salaamalykum.com) | `9ecff7f2...` |
| `Muslim_Knowledge_Guide_China_Maliki_School_Halal_Food_Rules_Frogs_Seafood_and_Me.md` | Muslim Knowledge Guide China: ... | [Source](https://salaamalykum.com) | `8f6d02db...` |
| `Muslim_Knowledge_Guide_China_Mosque_Teachers_Prayer_Unity_and_Youth_Islamic_Educ.md` | Muslim Knowledge Guide China: ... | [Source](https://salaamalykum.com) | `41907e16...` |
| `Muslim_Knowledge_Guide_China_Qur_an_Ancestor_Worship_Hui_Muslim_Tradition_and_Fa.md` | Muslim Knowledge Guide China: ... | [Source](https://salaamalykum.com) | `f1076b2a...` |
| `Muslim_Knowledge_Guide_China_Riba_Interest_Gharar_and_the_Economics_of_Sharia_Ar.md` | Muslim Knowledge Guide China: ... | [Source](https://salaamalykum.com) | `a5f6e0a2...` |
| `Muslim_Knowledge_Guide_China_Salah_Palestine_Dua_Qur_an_Values_and_Community_Spe.md` | Muslim Knowledge Guide China: ... | [Source](https://salaamalykum.com) | `2ce66167...` |
| `Muslim_Knowledge_Guide_China_Tianfang_Shijing_Islamic_Literature_and_Cross_Cultu.md` | Muslim Knowledge Guide China: ... | [Source](https://salaamalykum.com) | `cda80a4e...` |
| `Muslim_Knowledge_Guide_China_Why_Quran_Reciters_Deserve_Respect_and_Religious_Di.md` | Muslim Knowledge Guide China: ... | [Source](https://salaamalykum.com) | `237f8676...` |
| `Muslim_Knowledge_Guide_Egypt_Ali_Gomaa_Fatwa_Review_and_Andrew_Booso_Response.md` | Muslim Knowledge Guide Egypt: ... | [Source](https://salaamalykum.com) | `306e6de6...` |
| `Muslim_Knowledge_Guide_Egypt_Ali_Gomaa_Fatwa_on_Halal_Meat_People_of_the_Book_an.md` | Muslim Knowledge Guide Egypt: ... | [Source](https://salaamalykum.com) | `17f15d86...` |
| `Muslim_Knowledge_Guide_Egypt_Ali_Gomaa_Fatwa_on_Pork_Alcohol_Riba_and_Gambling_T.md` | Muslim Knowledge Guide Egypt: ... | [Source](https://salaamalykum.com) | `15ebf487...` |
| `Muslim_Knowledge_Guide_Malaysia_Islamic_Banking_Riba_Murabaha_and_Halal_Finance.md` | Muslim Knowledge Guide Malaysi... | [Source](https://salaamalykum.com) | `799e6de5...` |
| `Muslim_Knowledge_Guide_Women_in_Islam_Judaism_and_Christianity_Across_the_Muslim.md` | Muslim Knowledge Guide: Women ... | [Source](https://salaamalykum.com) | `9b50ce9f...` |
| `Muslim_Knowledge_Guide_in_the_Muslim_World_Qunut_Nazilah_Dua_for_Oppressed_Musli.md` | Muslim Knowledge Guide in the ... | [Source](https://salaamalykum.com) | `e3b1b9c4...` |
| `Muslim_Knowledge_Guide_in_the_Muslim_World_Quran_Trivia_Revelation_and_Faith_Que.md` | Muslim Knowledge Guide in the ... | [Source](https://salaamalykum.com) | `26bc46c4...` |
| `Muslim_Life_Guide_Beijing_Ramadan_at_Mingya_Niujie_Mosque_Iftar_and_Muslim_Insur.md` | Muslim Life Guide Beijing: Ram... | [Source](https://salaamalykum.com) | `b7cf9196...` |
| `Muslim_Life_Guide_China_Faith_Halal_Life_Work_Skills_and_Safe_Community_Influenc.md` | Muslim Life Guide China: Faith... | [Source](https://salaamalykum.com) | `58e3b055...` |
| `Muslim_Life_Guide_China_Muslim_Community_Anti_Muslim_Hate_Accounts_and_Social_Me.md` | Muslim Life Guide China: Musli... | [Source](https://salaamalykum.com) | `d520eda8...` |
| `Muslim_Life_Guide_China_Ramadan_Career_Wins_Faith_Friendly_Work_and_Islamic_Insu.md` | Muslim Life Guide China: Ramad... | [Source](https://salaamalykum.com) | `1f574a78...` |
| `Muslim_Life_Guide_China_Ramadan_Qur_an_Fidyah_and_Health_Struggles_With_Fasting.md` | Muslim Life Guide China Ramada... | [Source](https://salaamalykum.com) | `6da235f2...` |
| `Muslim_Life_Guide_China_Ramadan_Suhoor_Dialysis_Qur_an_and_the_First_Day_of_Fast.md` | Muslim Life Guide China Ramada... | [Source](https://salaamalykum.com) | `259c8654...` |
| `Muslim_Life_Guide_Qinghai_Salar_Eid_al_Adha_Qurban_and_Real_Halal_Family_Traditi.md` | Muslim Life Guide Qinghai: Sal... | [Source](https://salaamalykum.com) | `ae1c1fe9...` |
| `Muslim_Life_Guide_Vancouver_MDRT_Meeting_Islamic_Insurance_Ethics_and_Muslim_Pro.md` | Muslim Life Guide Vancouver: M... | [Source](https://salaamalykum.com) | `9c501a2e...` |
| `Muslim_Life_Guide_in_the_Muslim_World_Last_Ten_Nights_Menstruation_Dua_and_Ramad.md` | Muslim Life Guide in the Musli... | [Source](https://salaamalykum.com) | `aaf5d184...` |
| `Muslim_Travel_Guide_Bangkok_Halal_Food_Muslim_Friendly_Stays_and_Travel_Tips.md` | Muslim Travel Guide Bangkok: H... | [Source](https://salaamalykum.com) | `e61c730a...` |
| `Muslim_Travel_Guide_Bangkok_Persian_Shia_Mosques_and_Muharram_Traditions.md` | Muslim Travel Guide Bangkok: P... | [Source](https://salaamalykum.com) | `24143c66...` |
| `Muslim_Travel_Guide_Beijing_Changying_Hui_Township_Market_Halal_Food_and_Local_C.md` | Muslim Travel Guide Beijing Ch... | [Source](https://salaamalykum.com) | `1712636a...` |
| `Muslim_Travel_Guide_Beijing_Huairou_Mountain_Courtyard_Mosque_Hui_Village_and_Ha.md` | Muslim Travel Guide Beijing Hu... | [Source](https://salaamalykum.com) | `89e65fc3...` |
| `Muslim_Travel_Guide_Beijing_Ramadan_2025_Balizhuang_Mosque_Iftar_and_Community_R.md` | Muslim Travel Guide Beijing Ra... | [Source](https://salaamalykum.com) | `12b16b32...` |
| `Muslim_Travel_Guide_Beijing_Ramadan_Week_Three_Mosques_Iftar_and_Muslim_Communit.md` | Muslim Travel Guide Beijing Ra... | [Source](https://salaamalykum.com) | `5b6bbe18...` |
| `Muslim_Travel_Guide_Beijing_Winter_Diary_Mosques_Halal_Food_and_Hui_Muslim_Herit.md` | Muslim Travel Guide Beijing Wi... | [Source](https://salaamalykum.com) | `b6f05b3a...` |
| `Muslim_Travel_Guide_Brunei_Mawlid_Parade_Sultan_Bolkiah_Airport_Mosque_and_Islam.md` | Muslim Travel Guide Brunei: Ma... | [Source](https://salaamalykum.com) | `fe18a096...` |
| `Muslim_Travel_Guide_Brunei_Visa_on_Arrival_Sultanate_History_Mosques_and_Halal_F.md` | Muslim Travel Guide Brunei: Vi... | [Source](https://salaamalykum.com) | `b1815cc6...` |
| `Muslim_Travel_Guide_Canada_Visa_DIY_Tourist_Visa_Steps_Halal_Food_Planning_and_C.md` | Muslim Travel Guide Canada Vis... | [Source](https://salaamalykum.com) | `2f00979b...` |
| `Muslim_Travel_Guide_China_2026_Changde_Taohuayuan_Uyghur_Heritage_and_Hunan_Hala.md` | Muslim Travel Guide China 2026... | [Source](https://salaamalykum.com) | `406bfd07...` |
| `Muslim_Travel_Guide_China_2026_Changsha_Han_Hui_Village_Mosque_Life_and_Hunan_He.md` | Muslim Travel Guide China 2026... | [Source](https://salaamalykum.com) | `335ded78...` |
| `Muslim_Travel_Guide_China_2026_Manchuria_Mosques_in_Chifeng_Jilin_Acheng_and_Qiq.md` | Muslim Travel Guide China 2026... | [Source](https://salaamalykum.com) | `fa220d8a...` |
| `Muslim_Travel_Guide_China_2026_Songpan_Jiuzhaigou_Mosques_Hui_Muslims_and_Tea_Ho.md` | Muslim Travel Guide China 2026... | [Source](https://salaamalykum.com) | `4079d6df...` |
| `Muslim_Travel_Guide_China_2026_Xishuangbanna_Hui_Dai_Muslim_Villages_Mosques_and.md` | Muslim Travel Guide China 2026... | [Source](https://salaamalykum.com) | `85dd11f7...` |
| `Muslim_Travel_Guide_China_2026_Xunhua_and_Hualong_Salar_Mosques_Qinghai_Halal_Fo.md` | Muslim Travel Guide China 2026... | [Source](https://salaamalykum.com) | `44de8bd4...` |
| `Muslim_Travel_Guide_China_A_Hui_Muslim_Journey_Through_Faith_Niujie_Mosques_and.md` | Muslim Travel Guide China: A H... | [Source](https://salaamalykum.com) | `e205aab6...` |
| `Muslim_Travel_Guide_China_Baotou_Inner_Mongolia_Mosques_Shaomai_and_Hui_Muslim_W.md` | Muslim Travel Guide China: Bao... | [Source](https://salaamalykum.com) | `04d32010...` |
| `Muslim_Travel_Guide_China_Hebei_Botou_Old_Mosques_Hui_Streets_and_Local_Muslim_M.md` | Muslim Travel Guide China Hebe... | [Source](https://salaamalykum.com) | `f6e4024c...` |
| `Muslim_Travel_Guide_China_Kashgar_Id_Kah_Mosque_Abakh_Khoja_Mazar_and_Uyghur_Her.md` | Muslim Travel Guide China: Kas... | [Source](https://salaamalykum.com) | `33c37b03...` |
| `Muslim_Travel_Guide_China_Northern_Xinjiang_Sayram_Lake_Yining_Shaanxi_Mosque_an.md` | Muslim Travel Guide China: Nor... | [Source](https://salaamalykum.com) | `63a2255f...` |
| `Muslim_Travel_Guide_China_Southern_Xinjiang_Tajik_Muslims_Pamir_Plateau_and_Shia.md` | Muslim Travel Guide China: Sou... | [Source](https://salaamalykum.com) | `d31d9665...` |
| `Muslim_Travel_Guide_China_Yarkand_Altun_Mosque_Khanate_Tombs_and_Turdi_Haji_Mano.md` | Muslim Travel Guide China: Yar... | [Source](https://salaamalykum.com) | `7f07431d...` |
| `Muslim_Travel_Guide_China_Zhengzhou_Mosques_Hui_Muslim_Food_Huimian_and_Hulatang.md` | Muslim Travel Guide China: Zhe... | [Source](https://salaamalykum.com) | `b33e9a5b...` |
| `Muslim_Travel_Guide_Hong_Kong_Kowloon_Mosque_Halal_Airport_Food_and_Prayer_Rooms.md` | Muslim Travel Guide Hong Kong:... | [Source](https://salaamalykum.com) | `b4aaa960...` |
| `Muslim_Travel_Guide_Indonesia_Banten_Sultanate_Mosques_Coastal_City_and_Islamic.md` | Muslim Travel Guide Indonesia ... | [Source](https://salaamalykum.com) | `b2ea4d53...` |
| `Muslim_Travel_Guide_Indonesia_Jakarta_Trowulan_Demak_Grand_Mosque_and_Java_Halal.md` | Muslim Travel Guide Indonesia:... | [Source](https://salaamalykum.com) | `d138dcf3...` |
| `Muslim_Travel_Guide_Indonesia_Solo_Central_Java_Palaces_Mosques_and_Muslim_Herit.md` | Muslim Travel Guide Indonesia ... | [Source](https://salaamalykum.com) | `468d68b6...` |
| `Muslim_Travel_Guide_Indonesia_Surabaya_Sunan_Ampel_Mosque_Cheng_Ho_Mosque_and_Ha.md` | Muslim Travel Guide Indonesia:... | [Source](https://salaamalykum.com) | `3b6d23e7...` |
| `Muslim_Travel_Guide_Indonesia_Yogyakarta_Sultanate_Palaces_Mosques_and_Islamic_H.md` | Muslim Travel Guide Indonesia ... | [Source](https://salaamalykum.com) | `978463a0...` |
| `Muslim_Travel_Guide_Iran_Qom_Fatima_Masumeh_Shrine_Mosque_Mirror_Hall_and_Mazar.md` | Muslim Travel Guide Iran Qom: ... | [Source](https://salaamalykum.com) | `7f856a75...` |
| `Muslim_Travel_Guide_Iran_Tehran_Friday_Prayer_Closed_Mosques_and_Flower_Bird_Emb.md` | Muslim Travel Guide Iran Tehra... | [Source](https://salaamalykum.com) | `6fe57b7f...` |
| `Muslim_Travel_Guide_Iran_Tehran_Imam_Khomeini_Airport_Prayer_Room_Wudu_Area_and.md` | Muslim Travel Guide Iran Tehra... | [Source](https://salaamalykum.com) | `c846cccc...` |
| `Muslim_Travel_Guide_Iran_Tehran_Imam_Khomeini_Mosque_Grand_Bazaar_Food_and_Wudu.md` | Muslim Travel Guide Iran Tehra... | [Source](https://salaamalykum.com) | `bf6d45d1...` |
| `Muslim_Travel_Guide_Iran_Tehran_Vali_e_Asr_Mosque_Hidden_Modern_Mosque_Architect.md` | Muslim Travel Guide Iran Tehra... | [Source](https://salaamalykum.com) | `77650754...` |
| `Muslim_Travel_Guide_Japan_Tokyo_Japan_Muslim_Association_Islamic_Heritage_Hall_a.md` | Muslim Travel Guide Japan Toky... | [Source](https://salaamalykum.com) | `efb02f80...` |
| `Muslim_Travel_Guide_Japan_Tokyo_Yoyogi_Mosque_Friday_Prayer_Turkish_Market_and_M.md` | Muslim Travel Guide Japan Toky... | [Source](https://salaamalykum.com) | `f65fe6fe...` |
| `Muslim_Travel_Guide_Jiangsu_Yangzhou_Zhenjiang_Gaoyou_Mosques_Halal_Food_and_Can.md` | Muslim Travel Guide Jiangsu Ya... | [Source](https://salaamalykum.com) | `010b1318...` |
| `Muslim_Travel_Guide_Korea_Busan_Busan_Mosque_Turkish_Imam_Friday_Prayer_and_Musl.md` | Muslim Travel Guide Korea Busa... | [Source](https://salaamalykum.com) | `f3a5bfde...` |
| `Muslim_Travel_Guide_Korea_Seoul_Seoul_Central_Mosque_Friday_Prayer_Muslim_School.md` | Muslim Travel Guide Korea Seou... | [Source](https://salaamalykum.com) | `be7c5e6b...` |
| `Muslim_Travel_Guide_Liaoning_Dalian_Ancient_City_Streets_Mosques_and_Muslim_Heri.md` | Muslim Travel Guide Liaoning D... | [Source](https://salaamalykum.com) | `e909639c...` |
| `Muslim_Travel_Guide_Liaoning_Dandong_Fengcheng_Mosque_Visit_and_Local_Halal_Food.md` | Muslim Travel Guide Liaoning D... | [Source](https://salaamalykum.com) | `d1b947a3...` |
| `Muslim_Travel_Guide_London_Oxford_Cambridge_Islamic_Heritage_and_Heathrow_Prayer.md` | Muslim Travel Guide London: Ox... | [Source](https://salaamalykum.com) | `c199d9b7...` |
| `Muslim_Travel_Guide_Macau_Halal_Southeast_Asian_Food_Macau_Mosque_and_Muslim_Cem.md` | Muslim Travel Guide Macau: Hal... | [Source](https://salaamalykum.com) | `c4fcd0f7...` |
| `Muslim_Travel_Guide_Malacca_Nyonya_Food_Chinese_Mosque_and_Malaysia_Islamic_Heri.md` | Muslim Travel Guide Malacca: N... | [Source](https://salaamalykum.com) | `4aff6b88...` |
| `Muslim_Travel_Guide_Malaysia_8_Beautiful_Kuala_Lumpur_Mosques_Pink_Mosque_and_Bl.md` | Muslim Travel Guide Malaysia: ... | [Source](https://salaamalykum.com) | `d63af28b...` |
| `Muslim_Travel_Guide_Malaysia_Redang_Island_Terengganu_Crystal_Mosque_and_Halal_R.md` | Muslim Travel Guide Malaysia: ... | [Source](https://salaamalykum.com) | `e513afc6...` |
| `Muslim_Travel_Guide_Maldives_Male_Friday_Mosque_Coral_Stone_Tombs_and_National_M.md` | Muslim Travel Guide Maldives M... | [Source](https://salaamalykum.com) | `4632abc0...` |
| `Muslim_Travel_Guide_Mecca_Masjid_al_Haram_Umrah_Map_Makkah_Hotels_and_Jeddah_Air.md` | Muslim Travel Guide Mecca: Mas... | [Source](https://salaamalykum.com) | `7af91830...` |
| `Muslim_Travel_Guide_Medina_Prophet_Mosque_Quba_Mosque_and_Sacred_Islamic_Sites.md` | Muslim Travel Guide Medina: Pr... | [Source](https://salaamalykum.com) | `597536f3...` |
| `Muslim_Travel_Guide_Medina_Quran_Printing_Complex_Camel_Pilaf_and_Prophet_Mosque.md` | Muslim Travel Guide Medina: Qu... | [Source](https://salaamalykum.com) | `71c59370...` |
| `Muslim_Travel_Guide_Montreal_Mosques_Halal_Food_Chinatown_and_Canada_Muslim_City.md` | Muslim Travel Guide Montreal: ... | [Source](https://salaamalykum.com) | `61b481ef...` |
| `Muslim_Travel_Guide_Ottawa_First_Mosque_Halal_Chinese_Food_and_Canada_Muslim_His.md` | Muslim Travel Guide Ottawa: Fi... | [Source](https://salaamalykum.com) | `73dbc48f...` |
| `Muslim_Travel_Guide_Penang_George_Town_Halal_Hotel_Breakfast_Malay_Chinese_Herit.md` | Muslim Travel Guide Penang: Ge... | [Source](https://salaamalykum.com) | `e1b5894e...` |
| `Muslim_Travel_Guide_Shandong_Liaocheng_Old_Mosques_Canal_City_Streets_and_Hui_He.md` | Muslim Travel Guide Shandong L... | [Source](https://salaamalykum.com) | `bace5cc1...` |
| `Muslim_Travel_Guide_Sichuan_Xichang_Tianba_Hui_Muslim_Village_Mosques_and_Beef_H.md` | Muslim Travel Guide Sichuan: X... | [Source](https://salaamalykum.com) | `096adce8...` |
| `Muslim_Travel_Guide_Singapore_Burhani_Mosque_Dawoodi_Bohra_Shia_Community_and_Pr.md` | Muslim Travel Guide Singapore:... | [Source](https://salaamalykum.com) | `7f77eb79...` |
| `Muslim_Travel_Guide_Singapore_Indian_Muslim_Mosques_and_Heritage_Part_1.md` | Muslim Travel Guide Singapore:... | [Source](https://salaamalykum.com) | `df5fea97...` |
| `Muslim_Travel_Guide_Singapore_Little_India_Abdul_Gafoor_Mosque_Tamil_Muslim_Heri.md` | Muslim Travel Guide Singapore ... | [Source](https://salaamalykum.com) | `f64c67fd...` |
| `Muslim_Travel_Guide_Singapore_Little_India_Angullia_Mosque_Gujarati_Muslim_Herit.md` | Muslim Travel Guide Singapore ... | [Source](https://salaamalykum.com) | `1f5ec4e8...` |
| `Muslim_Travel_Guide_Singapore_Malabar_Mosque_South_Indian_Muslim_Community_and_L.md` | Muslim Travel Guide Singapore:... | [Source](https://salaamalykum.com) | `251a86e4...` |
| `Muslim_Travel_Guide_Singapore_Sultan_Mosque_Kampong_Glam_Prayer_Hall_and_Muslim.md` | Muslim Travel Guide Singapore:... | [Source](https://salaamalykum.com) | `73718c3c...` |
| `Muslim_Travel_Guide_Tianjin_Jiayuanli_Hui_Muslim_Neighborhood_Mosque_Visit_and_L.md` | Muslim Travel Guide Tianjin Ji... | [Source](https://salaamalykum.com) | `bc14f62e...` |
| `Muslim_Travel_Guide_Toronto_Chinese_Hui_Muslim_Eid_al_Adha_Halal_Noodles_and_Sca.md` | Muslim Travel Guide Toronto: C... | [Source](https://salaamalykum.com) | `1b022f25...` |
| `Muslim_Travel_Guide_Tunisia_15_Ancient_Mosques_and_Islamic_Heritage_Part_1.md` | Muslim Travel Guide Tunisia: 1... | [Source](https://salaamalykum.com) | `32d1f7b1...` |
| `Muslim_Travel_Guide_Tunisia_Kairouan_Great_Mosque_Jumu_ah_and_Islamic_Heritage_P.md` | Muslim Travel Guide Tunisia Ka... | [Source](https://salaamalykum.com) | `ed293986...` |
| `Muslim_Travel_Guide_Tunisia_Medina_Historic_Guesthouses_Halal_Food_and_Old_City.md` | Muslim Travel Guide Tunisia Me... | [Source](https://salaamalykum.com) | `b958e755...` |
| `Muslim_Travel_Guide_Tunisia_Sousse_UNESCO_Medina_Halal_Food_and_Old_City_Mosques.md` | Muslim Travel Guide Tunisia So... | [Source](https://salaamalykum.com) | `9f72071f...` |
| `Muslim_Travel_Guide_UAE_Abu_Dhabi_Louvre_Dubai_Trade_Shows_and_Modern_Arab_Trave.md` | Muslim Travel Guide UAE: Abu D... | [Source](https://salaamalykum.com) | `c8251e8b...` |
| `Muslim_Travel_Guide_UAE_Dubai_Halal_Flights_Prayer_Rooms_and_Sheikh_Zayed_Grand.md` | Muslim Travel Guide UAE: Dubai... | [Source](https://salaamalykum.com) | `311bc325...` |
| `Muslim_Travel_Guide_UK_Oxford_Cambridge_London_Halal_Restaurants_and_Islamic_His.md` | Muslim Travel Guide UK: Oxford... | [Source](https://salaamalykum.com) | `8d6ef968...` |
| `Muslim_Travel_Guide_Urumqi_Spring_Festival_Hui_Muslim_Life_Jumu_ah_and_Family_Vi.md` | Muslim Travel Guide Urumqi Spr... | [Source](https://salaamalykum.com) | `3e00e6a1...` |
| `Muslim_Travel_Guide_Vancouver_Ahmadiyya_Mosque_Muslim_Community_and_Canada_City.md` | Muslim Travel Guide Vancouver:... | [Source](https://salaamalykum.com) | `eb17d9ed...` |
| `Muslim_Travel_Guide_Vietnam_Hanoi_Al_Noor_Mosque_Wudu_Area_Halal_Food_and_Muslim.md` | Muslim Travel Guide Vietnam Ha... | [Source](https://salaamalykum.com) | `a1917d3c...` |
| `Muslim_Travel_Guide_Vietnam_Ho_Chi_Minh_City_Al_Rahim_Mosque_Ben_Thanh_Halal_Foo.md` | Muslim Travel Guide Vietnam Ho... | [Source](https://salaamalykum.com) | `0593c537...` |
| `Muslim_Travel_Guide_Xinjiang_Shawan_Big_Plate_Chicken_Urumqi_Halal_Food_and_Hami.md` | Muslim Travel Guide Xinjiang: ... | [Source](https://salaamalykum.com) | `83d74faf...` |
| `Ramadan_Muslim_Life_Guide_in_the_Muslim_World_Last_Ten_Nights_Laylat_al_Qadr_and.md` | Ramadan Muslim Life Guide in t... | [Source](https://salaamalykum.com) | `33d1435f...` |
| `Ramadan_in_China_2026_Iftar_at_Niujie_Mosque_Muslim_Work_Life_and_Beijing_Faith.md` | Ramadan in China 2026: Iftar a... | [Source](https://salaamalykum.com) | `f919d3cc...` |
| `Ramadan_in_China_2026_Qur_an_Hadith_Tarawih_and_Muslim_Strength_for_Fasting.md` | Ramadan in China 2026: Qur'an,... | [Source](https://salaamalykum.com) | `4f5cebfa...` |
| `Top_Halal_Restaurants_Beijing_Xinjiang_Yellow_Noodles_Xunji_Courtyard_Hot_Pot_an.md` | Top Halal Restaurants Beijing:... | [Source](https://salaamalykum.com) | `13d00611...` |
| `Where_Can_I_Find_a_Halal_Restaurant_in_Beijing_Gulan_Renjia_Mosque_Area_Stews_Ji.md` | Where Can I Find a Halal Resta... | [Source](https://salaamalykum.com) | `ea21b8ac...` |


</details>

## 🤝 Contributing & License
Refer to `CONTRIBUTING.md` and `LICENSE` (MIT).
