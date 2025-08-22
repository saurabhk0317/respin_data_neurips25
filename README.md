# RESPIN S1.0 Speech Corpus

Welcome! This repository provides access to the **RESPIN-S1.0 Speech Corpus** — a large-scale multilingual dataset spanning **9 languages** and **38 dialects**. Due to its size (>1TB), the dataset is split into smaller tar files for easier download and management.

---

## 📊 Dataset Overview

- **Total Files:** 63 (54 tar files + 9 lexicon files)
- **Languages:** 9
- **Dialects:** 38
- **Data Splits:** `small`, `clean`, `seminoisy`, `noisy`, `dev`, `test`
- **Verification:** Dev and test sets are manually verified

Each language includes:
- 6 tar files (for different splits)
- 1 lexicon file

---

## ⬇️ Steps to Download the Dataset

See the [Dataset URLs](#dataset-urls) section below for direct download links, organized by language and split.

---

## Data Statistics ##

- Type: Parallel Speech and Text
- Language(s): Bengali (bn), Bhojpuri (bh), Chhattisgarhi (ch), Hindi (hi), Kannada (kn), Magahi (mg), Maithili (mt), Marathi (mr), Telugu (te)
- Linguality: Multilingual
- Catalogue Id: RESPIN-S1.0
- Total Audio Duration (HH:MM:SS): 12652:50:00
- Average Sample Duration: 5.35 secs
- Total Unique Text IDs: 203536
- Recording Specifications: 16 kHz, 16 bits per sample, Mono
- Recording Format: WAV
- Recording Environment: Natural
- Data creator: Indian Institute of Sciences (IISc), Bengaluru
- Year of publishing: 2024
- Suggested research purposes / areas: ASR, Language Identification, Dialect Identification, etc.

### Language-wise stats ###
| DID   | #utt | #sent (Agri) | #sent (Bank) | #sent | #spk | #re-spk | Agri (hrs) | Bank (hrs) | Total (hrs) |
|-------|------|--------------|--------------|-------|------|---------|------------|------------|-------------|
| dev_bh | 1500 | 334 | 241 | 575 | 60 | 60 | 1.20 | 0.94 | 2.14 |
| dev_bn | 1500 | 291 | 203 | 494 | 100 | 100 | 1.33 | 0.94 | 2.27 |
| dev_ch | 1413 | 281 | 230 | 511 | 80 | 80 | 1.32 | 1.08 | 2.40 |
| dev_hi | 1539 | 388 | 334 | 722 | 100 | 100 | 1.17 | 1.03 | 2.21 |
| dev_kn | 1430 | 287 | 231 | 518 | 100 | 100 | 1.35 | 1.02 | 2.37 |
| dev_mg | 1431 | 235 | 259 | 494 | 80 | 80 | 0.96 | 1.14 | 2.10 |
| dev_mr | 1386 | 251 | 258 | 509 | 80 | 80 | 0.94 | 1.03 | 1.98 |
| dev_mt | 1409 | 405 | 288 | 693 | 80 | 80 | 1.17 | 0.89 | 2.06 |
| dev_te | 1438 | 265 | 235 | 500 | 80 | 80 | 1.21 | 1.09 | 2.30 |
| test_bh | 2220 | 390 | 304 | 694 | 120 | 120 | 1.68 | 1.42 | 3.10 |
| test_bn | 2174 | 363 | 285 | 648 | 200 | 200 | 1.87 | 1.39 | 3.26 |
| test_ch | 2234 | 388 | 307 | 695 | 160 | 160 | 2.13 | 1.72 | 3.85 |
| test_hi | 2288 | 453 | 400 | 853 | 201 | 201 | 1.74 | 1.57 | 3.30 |
| test_kn | 2161 | 349 | 314 | 663 | 200 | 200 | 2.00 | 1.60 | 3.61 |
| test_mg | 2193 | 325 | 315 | 640 | 160 | 160 | 1.56 | 1.62 | 3.17 |
| test_mr | 2170 | 343 | 368 | 711 | 160 | 160 | 1.51 | 1.53 | 3.04 |
| test_mt | 2172 | 535 | 458 | 993 | 160 | 160 | 1.80 | 1.53 | 3.33 |
| test_te | 2226 | 336 | 316 | 652 | 160 | 160 | 1.67 | 1.70 | 3.37 |
| train_bh_clean | 694738 | 12062 | 9905 | 21967 | 1851 | 1344 | 472.01 | 417.60 | 889.61 |
| train_bh_noisy | 43543 | 8300 | 6956 | 15256 | 1392 | 858 | 36.12 | 32.41 | 68.53 |
| train_bh_seminoisy | 58179 | 9057 | 7436 | 16493 | 1505 | 1053 | 48.27 | 43.56 | 91.83 |
| train_bh_small | 95280 | 9760 | 9296 | 19056 | 1445 | 1079 | 70.33 | 72.65 | 142.98 |
| train_bn_clean | 645791 | 11847 | 8340 | 20187 | 1791 | 1655 | 509.47 | 385.13 | 894.60 |
| train_bn_noisy | 6587 | 2997 | 2396 | 5393 | 805 | 222 | 3.22 | 2.55 | 5.77 |
| train_bn_seminoisy | 92208 | 10225 | 7541 | 17766 | 1479 | 1265 | 90.39 | 72.45 | 162.84 |
| train_bn_small | 85800 | 9098 | 8062 | 17160 | 1280 | 1184 | 79.76 | 63.20 | 142.96 |
| train_ch_clean | 640649 | 9904 | 9496 | 19400 | 2082 | 1534 | 503.30 | 505.79 | 1009.09 |
| train_ch_noisy | 36486 | 7316 | 7140 | 14456 | 2024 | 1424 | 36.12 | 37.84 | 73.96 |
| train_ch_seminoisy | 78942 | 8731 | 8603 | 17334 | 2048 | 1511 | 77.95 | 83.33 | 161.28 |
| train_ch_small | 85800 | 8802 | 8358 | 17160 | 1586 | 1237 | 85.64 | 89.58 | 175.22 |
| train_hi_clean | 574544 | 9720 | 9625 | 19345 | 2305 | 2216 | 355.48 | 357.14 | 712.61 |
| train_hi_noisy | 186275 | 9686 | 9600 | 19286 | 2314 | 2221 | 150.06 | 154.49 | 304.55 |
| train_hi_seminoisy | 181710 | 9629 | 9551 | 19180 | 2304 | 2220 | 134.31 | 138.96 | 273.27 |
| train_hi_small | 85800 | 8573 | 8587 | 17160 | 2172 | 1960 | 63.75 | 64.73 | 128.47 |
| train_kn_clean | 554398 | 12142 | 11152 | 23294 | 1931 | 1703 | 466.27 | 422.45 | 888.72 |
| train_kn_noisy | 97806 | 11484 | 10434 | 21918 | 1939 | 1687 | 102.40 | 88.78 | 191.18 |
| train_kn_seminoisy | 104324 | 11520 | 10484 | 22004 | 1919 | 1698 | 108.21 | 94.21 | 202.42 |
| train_kn_small | 85800 | 8539 | 8621 | 17160 | 1859 | 1563 | 84.81 | 80.02 | 164.83 |
| train_mg_clean | 769679 | 10583 | 10917 | 21500 | 2078 | 1997 | 524.83 | 541.48 | 1066.30 |
| train_mg_noisy | 36206 | 7349 | 7594 | 14943 | 2025 | 1850 | 28.84 | 31.34 | 60.18 |
| train_mg_seminoisy | 53414 | 8006 | 8355 | 16361 | 2037 | 1897 | 43.25 | 48.05 | 91.30 |
| train_mg_small | 95280 | 9528 | 9528 | 19056 | 1493 | 1357 | 77.29 | 80.47 | 157.77 |
| train_mr_clean | 809934 | 11176 | 11893 | 23069 | 2644 | 2148 | 499.77 | 526.29 | 1026.06 |
| train_mr_noisy | 109910 | 9883 | 10423 | 20306 | 2634 | 2108 | 85.62 | 88.54 | 174.16 |
| train_mr_seminoisy | 191098 | 10541 | 11128 | 21669 | 2629 | 2142 | 144.52 | 140.94 | 285.46 |
| train_mr_small | 95280 | 9528 | 9528 | 19056 | 2305 | 1742 | 69.92 | 70.56 | 140.49 |
| train_mt_clean | 392739 | 12623 | 10485 | 23108 | 1917 | 1825 | 294.66 | 257.49 | 552.16 |
| train_mt_noisy | 174313 | 12300 | 10309 | 22609 | 1934 | 1824 | 159.58 | 154.63 | 314.21 |
| train_mt_seminoisy | 237484 | 12642 | 10512 | 23154 | 1916 | 1832 | 213.43 | 186.61 | 400.04 |
| train_mt_small | 95280 | 9546 | 9510 | 19056 | 1913 | 1745 | 78.99 | 80.33 | 159.32 |
| train_te_clean | 702883 | 10012 | 9966 | 19978 | 2287 | 1819 | 503.27 | 517.90 | 1021.16 |
| train_te_noisy | 73390 | 8972 | 8942 | 17914 | 2258 | 1747 | 63.19 | 64.47 | 127.66 |
| train_te_seminoisy | 111471 | 9678 | 9692 | 19370 | 2273 | 1819 | 91.33 | 94.77 | 186.10 |
| train_te_small | 95280 | 9527 | 9529 | 19056 | 1848 | 1415 | 77.17 | 78.72 | 155.89 |



### Lexicon Statistics ###
| LID | #chars | #phones | #words |
|-----|--------|---------|--------|
| bh  | 71     | 54      | 14105   |
| bn  | 64     | 50      | 18571   |
| ch  | 68     | 50      | 13230   |
| hi  | 72     | 55      | 16571   |
| kn  | 66     | 50      | 50822   |
| mg  | 72     | 54      | 21711   |
| mr  | 68     | 51      | 35709   |
| mt  | 72     | 55      | 19336   |
| te  | 63     | 48      | 39235   |

### Directory Structure ###
```
train_bn_small/
├── D1
│   ├── <speaker_id>
│   │   ├── IISc_RESPIN_<lid>_<dialect>_<speaker_id>_<pincode>_<genderTag>_<domainTag>_<text_id>_<uttid>.wav
│   │   ├── [...]
│   │   └── IISc_RESPIN_<lid>_<dialect>_<speaker_id>.txt
│   ├── [...]
├── D2
│   ├── [...]
├── [...]
└── meta_train_bn_small.json
└── README.md
```

### Metadata File Sample (meta_dev_bn.json) ###
```json
{
    "IISc_RESPIN_bn_D3_21023_700096_F_AGRI_209142_20001411": {
        "age_group": "41-45",
        "age_group_reassigned": "41-45",
        "dialect": "D3",
        "domain": "Agriculture",
        "duration": 6.24,
        "gender": "FEMALE",
        "gender_reassigned": "FEMALE",
        "lid": "bn",
        "pincode": "700096",
        "slab": "clean",
        "speaker_id": "21023",
        "speaker_id_reassigned": "21023_2",
        "text": "চিকেন হারভেস্টার মেশিনে পোল্ট্রি ফার্মের মুরগি জবাই করে",
        "text_id": "209142",
        "text_type": "statement",
        "utterance_id": "20001411",
        "wav_path": "D3/21023/IISc_RESPIN_bn_D3_21023_700096_F_AGRI_209142_20001411.wav"
    },
    "IISc_RESPIN_bn_D3_21046_700153_F_AGRI_208885_20002724": {
        "age_group": "46-50",
        "age_group_reassigned": "46-50",
        "dialect": "D3",
        "domain": "Agriculture",
        "duration": 10.34,
        "gender": "FEMALE",
        "gender_reassigned": "FEMALE",
        "lid": "bn",
        "pincode": "700153",
        "slab": "clean",
        "speaker_id": "21046",
        "speaker_id_reassigned": "21046_2",
        "text": "জোয়ান বা ক্যারম সীড ভিটামিন এবং অ্যান্টিঅক্সিডেন্টে পরিপূর্ণ",
        "text_id": "208885",
        "text_type": "statement",
        "utterance_id": "20002724",
        "wav_path": "D3/21046/IISc_RESPIN_bn_D3_21046_700153_F_AGRI_208885_20002724.wav"
    }
}
```

### Text File Sample (IISc_RESPIN_bn_D3_21023.txt) ###
```
IISc_RESPIN_bn_D3_21023_700096_F_AGRI_209142_20001411	চিকেন হারভেস্টার মেশিনে পোল্ট্রি ফার্মের মুরগি জবাই করে
IISc_RESPIN_bn_D3_21023_700096_F_AGRI_208764_20011396	উড ওয়ার্ম হচ্ছে এক ধরণের পোকা যেটা কাঠের ভেতরে বাসা বেঁধে কাঠকে ক্ষইয়ে দেয়
IISc_RESPIN_bn_D3_21023_700096_F_AGRI_208576_20011401	রিচ গোর্ড বা ঝিঙে হল এক রকমের পুষ্টিকর সবজি যেটিকে আমরা খাদ্য হিসেবে গ্রহণ করি
```

---

## RESPIN Dataset Loader

A lightweight, HuggingFace-style loader for RESPIN, using Croissant metadata.

---

### 🚀 Features

- Download individual or grouped RESPIN subsets
- Verifies SHA256 checksums and handles corrupted downloads
- Extracts and loads metadata (`meta_*.json`) with absolute `wav_path`s
- HuggingFace-style API: `load("train_bh")`, `load("test")`, etc.
- **No external dependencies** (uses only Python standard library)

---

### 📦 Installation

No installation required — simply copy the `RESPINDataset` class into your Python script or module.

---

### 📝 Example Usage

```python
from respin_loader import RESPINDataset  # or paste RESPINDataset class directly

# Initialize the dataset loader with metadata and cache directory
dataset = RESPINDataset(
	metadata_path="metadata.json",
	cache_dir="path/to/download/directory/RESPIN_data"
)
```

#### ✅ Load a single subset

```python
# Load development set for Chhattisgarhi
data = dataset.load("dev_ch")
```

#### ✅ Load all dev sets

```python
data = dataset.load("dev")
```

#### ✅ Load all train subsets

```python
data = dataset.load("train")
```

#### ✅ Load all train subsets for a specific language

```python
# All Bhojpuri training subsets: clean, noisy, seminoisy, small
data = dataset.load("train_bh")
```

---

### 📂 Data Format

Each entry in the loaded dataset looks like:

```json
{
  "age_group": "41-45",
  "dialect": "D1",
  "domain": "Banking",
  "duration": 12.07,
  "gender": "MALE",
  "lid": "ch",
  "pincode": "495001",
  "speaker_id": "30060",
  "text": "सब्जी भाजी के भाव ह आज...",
  "text_id": "303070",
  "utterance_id": "30000010",
  "wav_path": "/absolute/path/to/.../D1/30060/IISc_RESPIN_ch_....wav"
}
```

---

### 💡 Notes

- Files are only downloaded once unless the checksum fails.
- Corrupt or partial downloads are deleted and restarted automatically.
- `.tar.gz` archives are extracted directly into the cache directory, each containing:
  - A folder named like the archive (e.g., `IISc_RESPIN_train_bn_clean/`)
  - A `meta_*.json` file inside
  - A README.md file inside
- `wav_path` is automatically updated to the absolute file path for convenience.
- Fully compatible with standard Python code — **no external dependencies required**.

---


## Dataset URLs

Below are the download links for the complete dataset, organized by language:

#### Bengali
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/bengali/IISc_RESPIN_dev_bn.tar.gz](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/bengali/IISc_RESPIN_dev_bn.tar.gz)
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/bengali/IISc_RESPIN_lexicon_bn.txt](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/bengali/IISc_RESPIN_lexicon_bn.txt)
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/bengali/IISc_RESPIN_train_bn_clean.tar.gz](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/bengali/IISc_RESPIN_train_bn_clean.tar.gz)
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/bengali/IISc_RESPIN_train_bn_noisy.tar.gz](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/bengali/IISc_RESPIN_train_bn_noisy.tar.gz)
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/bengali/IISc_RESPIN_train_bn_seminoisy.tar.gz](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/bengali/IISc_RESPIN_train_bn_seminoisy.tar.gz)
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/bengali/IISc_RESPIN_train_bn_small.tar.gz](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/bengali/IISc_RESPIN_train_bn_small.tar.gz)

#### Bhojpuri
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/bhojpuri/IISc_RESPIN_dev_bh.tar.gz](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/bhojpuri/IISc_RESPIN_dev_bh.tar.gz)
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/bhojpuri/IISc_RESPIN_lexicon_bh.txt](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/bhojpuri/IISc_RESPIN_lexicon_bh.txt)
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/bhojpuri/IISc_RESPIN_train_bh_clean.tar.gz](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/bhojpuri/IISc_RESPIN_train_bh_clean.tar.gz)
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/bhojpuri/IISc_RESPIN_train_bh_noisy.tar.gz](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/bhojpuri/IISc_RESPIN_train_bh_noisy.tar.gz)
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/bhojpuri/IISc_RESPIN_train_bh_seminoisy.tar.gz](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/bhojpuri/IISc_RESPIN_train_bh_seminoisy.tar.gz)
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/bhojpuri/IISc_RESPIN_train_bh_small.tar.gz](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/bhojpuri/IISc_RESPIN_train_bh_small.tar.gz)

#### Chhattisgarhi
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/chhattisgarhi/IISc_RESPIN_dev_ch.tar.gz](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/chhattisgarhi/IISc_RESPIN_dev_ch.tar.gz)
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/chhattisgarhi/IISc_RESPIN_lexicon_ch.txt](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/chhattisgarhi/IISc_RESPIN_lexicon_ch.txt)
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/chhattisgarhi/IISc_RESPIN_train_ch_clean.tar.gz](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/chhattisgarhi/IISc_RESPIN_train_ch_clean.tar.gz)
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/chhattisgarhi/IISc_RESPIN_train_ch_noisy.tar.gz](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/chhattisgarhi/IISc_RESPIN_train_ch_noisy.tar.gz)
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/chhattisgarhi/IISc_RESPIN_train_ch_seminoisy.tar.gz](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/chhattisgarhi/IISc_RESPIN_train_ch_seminoisy.tar.gz)
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/chhattisgarhi/IISc_RESPIN_train_ch_small.tar.gz](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/chhattisgarhi/IISc_RESPIN_train_ch_small.tar.gz)

#### Hindi
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/hindi/IISc_RESPIN_dev_hi.tar.gz](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/hindi/IISc_RESPIN_dev_hi.tar.gz)
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/hindi/IISc_RESPIN_lexicon_hi.txt](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/hindi/IISc_RESPIN_lexicon_hi.txt)
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/hindi/IISc_RESPIN_train_hi_clean.tar.gz](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/hindi/IISc_RESPIN_train_hi_clean.tar.gz)
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/hindi/IISc_RESPIN_train_hi_noisy.tar.gz](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/hindi/IISc_RESPIN_train_hi_noisy.tar.gz)
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/hindi/IISc_RESPIN_train_hi_seminoisy.tar.gz](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/hindi/IISc_RESPIN_train_hi_seminoisy.tar.gz)
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/hindi/IISc_RESPIN_train_hi_small.tar.gz](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/hindi/IISc_RESPIN_train_hi_small.tar.gz)

#### Kannada
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/kannada/IISc_RESPIN_dev_kn.tar.gz](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/kannada/IISc_RESPIN_dev_kn.tar.gz)
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/kannada/IISc_RESPIN_lexicon_kn.txt](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/kannada/IISc_RESPIN_lexicon_kn.txt)
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/kannada/IISc_RESPIN_train_kn_clean.tar.gz](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/kannada/IISc_RESPIN_train_kn_clean.tar.gz)
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/kannada/IISc_RESPIN_train_kn_noisy.tar.gz](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/kannada/IISc_RESPIN_train_kn_noisy.tar.gz)
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/kannada/IISc_RESPIN_train_kn_seminoisy.tar.gz](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/kannada/IISc_RESPIN_train_kn_seminoisy.tar.gz)
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/kannada/IISc_RESPIN_train_kn_small.tar.gz](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/kannada/IISc_RESPIN_train_kn_small.tar.gz)

#### Magahi
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/magahi/IISc_RESPIN_dev_mg.tar.gz](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/magahi/IISc_RESPIN_dev_mg.tar.gz)
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/magahi/IISc_RESPIN_lexicon_mg.txt](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/magahi/IISc_RESPIN_lexicon_mg.txt)
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/magahi/IISc_RESPIN_train_mg_clean.tar.gz](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/magahi/IISc_RESPIN_train_mg_clean.tar.gz)
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/magahi/IISc_RESPIN_train_mg_noisy.tar.gz](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/magahi/IISc_RESPIN_train_mg_noisy.tar.gz)
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/magahi/IISc_RESPIN_train_mg_seminoisy.tar.gz](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/magahi/IISc_RESPIN_train_mg_seminoisy.tar.gz)
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/magahi/IISc_RESPIN_train_mg_small.tar.gz](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/magahi/IISc_RESPIN_train_mg_small.tar.gz)

#### Maithili
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/maithili/IISc_RESPIN_dev_mt.tar.gz](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/maithili/IISc_RESPIN_dev_mt.tar.gz)
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/maithili/IISc_RESPIN_lexicon_mt.txt](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/maithili/IISc_RESPIN_lexicon_mt.txt)
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/maithili/IISc_RESPIN_train_mt_clean.tar.gz](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/maithili/IISc_RESPIN_train_mt_clean.tar.gz)
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/maithili/IISc_RESPIN_train_mt_noisy.tar.gz](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/maithili/IISc_RESPIN_train_mt_noisy.tar.gz)
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/maithili/IISc_RESPIN_train_mt_seminoisy.tar.gz](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/maithili/IISc_RESPIN_train_mt_seminoisy.tar.gz)
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/maithili/IISc_RESPIN_train_mt_small.tar.gz](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/maithili/IISc_RESPIN_train_mt_small.tar.gz)

#### Marathi
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/marathi/IISc_RESPIN_dev_mr.tar.gz](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/marathi/IISc_RESPIN_dev_mr.tar.gz)
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/marathi/IISc_RESPIN_lexicon_mr.txt](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/marathi/IISc_RESPIN_lexicon_mr.txt)
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/marathi/IISc_RESPIN_train_mr_clean.tar.gz](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/marathi/IISc_RESPIN_train_mr_clean.tar.gz)
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/marathi/IISc_RESPIN_train_mr_noisy.tar.gz](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/marathi/IISc_RESPIN_train_mr_noisy.tar.gz)
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/marathi/IISc_RESPIN_train_mr_seminoisy.tar.gz](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/marathi/IISc_RESPIN_train_mr_seminoisy.tar.gz)
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/marathi/IISc_RESPIN_train_mr_small.tar.gz](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/marathi/IISc_RESPIN_train_mr_small.tar.gz)

#### Telugu
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/telugu/IISc_RESPIN_dev_te.tar.gz](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/telugu/IISc_RESPIN_dev_te.tar.gz)
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/telugu/IISc_RESPIN_lexicon_te.txt](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/telugu/IISc_RESPIN_lexicon_te.txt)
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/telugu/IISc_RESPIN_train_te_clean.tar.gz](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/telugu/IISc_RESPIN_train_te_clean.tar.gz)
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/telugu/IISc_RESPIN_train_te_noisy.tar.gz](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/telugu/IISc_RESPIN_train_te_noisy.tar.gz)
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/telugu/IISc_RESPIN_train_te_seminoisy.tar.gz](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/telugu/IISc_RESPIN_train_te_seminoisy.tar.gz)
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/telugu/IISc_RESPIN_train_te_small.tar.gz](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/telugu/IISc_RESPIN_train_te_small.tar.gz)

#### Test sets

- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/test_set/IISc_RESPIN_test_bh.tar.gz](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/test_set/IISc_RESPIN_test_bh.tar.gz)
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/test_set/IISc_RESPIN_test_bn.tar.gz](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/test_set/IISc_RESPIN_test_bn.tar.gz)
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/test_set/IISc_RESPIN_test_ch.tar.gz](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/test_set/IISc_RESPIN_test_ch.tar.gz)
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/test_set/IISc_RESPIN_test_hi.tar.gz](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/test_set/IISc_RESPIN_test_hi.tar.gz)
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/test_set/IISc_RESPIN_test_kn.tar.gz](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/test_set/IISc_RESPIN_test_kn.tar.gz)
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/test_set/IISc_RESPIN_test_mg.tar.gz](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/test_set/IISc_RESPIN_test_mg.tar.gz)
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/test_set/IISc_RESPIN_test_mr.tar.gz](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/test_set/IISc_RESPIN_test_mr.tar.gz)
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/test_set/IISc_RESPIN_test_mt.tar.gz](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/test_set/IISc_RESPIN_test_mt.tar.gz)
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/test_set/IISc_RESPIN_test_te.tar.gz](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/test_set/IISc_RESPIN_test_te.tar.gz)
---
