# RESPIN S1.0 Speech Corpus

This repository provides links to the RESPIN S1.0 Speech Corpus. Due to its large size (>1TB), the dataset is divided into smaller tar files. It includes data for **9 languages** and **38 dialects**, with each language containing 5 tar files and a lexicon file. The dataset is categorized into **small**, **clean**, **semi-noisy**, and **noisy** splits, along with **dev** and **test** sets. The dev and test sets have been manually verified.

---

## Dataset Overview

- **Total Files**: 63 (54 tar files + 9 lexicon/txt files)
- **Languages**: 9
- **Dialects**: 38
- **Data Splits**: Small, Clean, Semi-Noisy, Noisy, Dev, Test

---

## Steps to Download the Dataset

To download a specific tar file, use the following Python script:

```python
from datasets import load_dataset, DownloadConfig

# Load a specific subset (e.g., Maithili dev) of the RESPIN dataset
dataset = load_dataset(
	path="dataset.py",             # Path to your local dataset loading script
	name="mt_dev",                 # Must match a BUILDER_CONFIG name (e.g., "mt_dev", "bh_train_clean", etc.)
	split="validation",            # Optional: specify 'train', 'validation', or 'test'
	cache_dir="hf_cache",          # Optional: cache directory for shared use across projects
	download_config=DownloadConfig(
		cache_dir="downloads",     # Local cache directory for downloaded .tar.gz files
		resume_download=True,      # Resume partial downloads if interrupted
		use_etag=True              # Use ETag to avoid unnecessary re-downloads
	),
	trust_remote_code=True,        # Required for loading local dataset.py
	keep_in_memory=False,          # Set True to load the full dataset into memory (default False)
	verification_mode="no_checks"  # Faster load if you trust the data
)
```

---

### Example Usage

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

### Access a Sample Record
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
- Use the `resume_download` option to handle interruptions during downloads.
- For more details, refer to the dataset loading script (`dataset.py`).
