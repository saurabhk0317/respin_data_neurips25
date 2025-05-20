# RESPIN S1.0 Speech Corpus

This repository provides links to the RESPIN S1.0 Speech Corpus. Due to its large size (>1TB), the dataset is divided into smaller tar files. It includes data for **9 languages** and **38 dialects**, with each language containing 5 tar files and a lexicon file. The dataset is categorized into **small**, **clean**, **semi-noisy**, and **noisy** splits, along with **dev** and **test** sets. The dev and test sets have been manually verified.

---

## Dataset Overview

- **Total Files**: 63 (54 tar files + 9 lexicon/txt files)
- **Languages**: 9
- **Dialects**: 38
- **Data Splits**: Small, Clean, Seminoisy, Noisy, Dev, Test

---

## Steps to Download the Dataset

# RESPIN Dataset Loader

A HuggingFace-style lightweight loader for the RESPIN multilingual speech dataset using Croissant metadata.

---

## 🚀 Features

- ✅ Download individual or grouped RESPIN subsets
- ✅ Verifies SHA256 checksums and handles corrupted downloads
- ✅ Extracts and loads metadata (`meta_*.json`) with absolute `wav_path`s
- ✅ HuggingFace-style `load("train_bh")`, `load("test")`, etc.
- ✅ No external dependencies (uses Python standard library)

---

## 📦 Installation

No installation needed — just copy `RESPINDataset` into your Python script or module.

---

## 📝 Example Usage

```python
from respin_loader import RESPINDataset  # or paste RESPINDataset class directly

# Initialize the dataset loader with metadata and cache directory
dataset = RESPINDataset(
    metadata_path="metadata.json",
    cache_dir="path/to/download/directory/RESPIN_data"
)
```

### ✅ Load a single subset
```python
# Load development set for Chhattisgarhi
data = dataset.load("dev_ch")
```

### ✅ Load all dev sets
```python
# Load development set for Chhattisgarhi
data = dataset.load("dev_ch")
```

### ✅ Load all train subsets
```python
# Load development set for Chhattisgarhi
data = dataset.load("dev_ch")
```

### ✅ Load all train subsets for a specific language
```python
# Load development set for Chhattisgarhi
data = dataset.load("dev_ch")
```

#### Inspect the Dataset
```python
>>> print(dataset)
DatasetDict({
	validation: Dataset({
		features: ['utterance_id', 'text', 'wav_path', 'dialect', 'gender', 'age_group', 'domain', 'speaker_id', 'pincode', 'duration'],
		num_rows: 1409
	})
})
```

#### Access a Sample Record
```python
>>> print(dataset['validation'][0])  # or: print(dataset[0]) depending on split format
{
	'utterance_id': 'IISc_RESPIN_mt_D1_80218_852112_M_BANK_804004_80002378',
	'text': 'गाड़ीक बीमा एकटा समझौता छै गाड़ी मालिक आ इंश्योरेंस कंपनी केर बीचक',
	'wav_path': 'downloads/mt/IISc_RESPIN_dev_mt/D1/80218/IISc_RESPIN_mt_D1_80218_852112_M_BANK_804004_80002378.wav',
	'dialect': 'D1',
	'gender': 'MALE',
	'age_group': '25-30',
	'domain': 'Banking',
	'speaker_id': '80218',
	'pincode': '852112',
	'duration': 9.100000381469727
}
```

---

## Notes

- Ensure you have sufficient storage space before downloading the dataset.
- For more details, refer to the dataset loading script (`dataset.py`).

### Dataset URLs

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

- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/test_set/IISc_RESPIN_test_mr.tar.gz](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/test_set/IISc_RESPIN_test_mr.tar.gz)
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/test_set/IISc_RESPIN_test_bh.tar.gz](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/test_set/IISc_RESPIN_test_bh.tar.gz)
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/test_set/IISc_RESPIN_test_ch.tar.gz](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/test_set/IISc_RESPIN_test_ch.tar.gz)
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/test_set/IISc_RESPIN_test_te.tar.gz](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/test_set/IISc_RESPIN_test_te.tar.gz)
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/test_set/IISc_RESPIN_test_mg.tar.gz](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/test_set/IISc_RESPIN_test_mg.tar.gz)
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/test_set/IISc_RESPIN_test_kn.tar.gz](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/test_set/IISc_RESPIN_test_kn.tar.gz)
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/test_set/IISc_RESPIN_test_mt.tar.gz](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/test_set/IISc_RESPIN_test_mt.tar.gz)
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/test_set/IISc_RESPIN_test_bn.tar.gz](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/test_set/IISc_RESPIN_test_bn.tar.gz)
- [https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/test_set/IISc_RESPIN_test_hi.tar.gz](https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/test_set/IISc_RESPIN_test_hi.tar.gz)