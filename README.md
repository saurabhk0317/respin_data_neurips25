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
--
