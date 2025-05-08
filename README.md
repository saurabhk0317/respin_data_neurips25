# respin_data_neurips25

This repository contains links for the RESPIN S1.0 Speech corpus. Since the data size is huge (> 1TB ), the dataset is split into smaller tar files. 
The dataset consists of 9 languages, 38 dialects in total, each language contains 5 tar files and a lexicon file.
The dataset contains: small, clean, semi-noisy and noisy, dev and test data splits. 
Dev set and test set is manually checked.
## Steps to download the dataset:

There are total 63 files (54 tar and 9 lexicon/txt files):
In order to downlaod a particular tar file, you can call the below python script.

```
from datasets import load_dataset, DownloadConfig
dataset = load_dataset("dataset.py", name="mt_dev", \
download_config=DownloadConfig(cache_dir="downloads"))
```