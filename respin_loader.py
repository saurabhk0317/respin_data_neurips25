import os
import json
import hashlib
import tarfile
import urllib.request
from pathlib import Path
from typing import Union

class RESPINDataset:
    def __init__(self, metadata_path: str, cache_dir: str = "downloads"):
        with open(metadata_path, "r") as f:
            self.metadata = json.load(f)
        self.cache_dir = Path(cache_dir)
        self.distributions = self.metadata["distribution"]

    def _compute_sha256(self, file_path):
        sha256 = hashlib.sha256()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(8192), b""):
                sha256.update(chunk)
        return sha256.hexdigest()

    def _download_file(self, url, tar_path, expected_sha256):
        self.cache_dir.mkdir(parents=True, exist_ok=True)

        # Always (re)download if file does not exist or fails checksum
        needs_download = True
        if tar_path.exists():
            print(f"⚠️  Found existing file: {tar_path.name}, verifying checksum...")
            actual_sha = self._compute_sha256(tar_path)
            if actual_sha == expected_sha256:
                print(f"✅ SHA256 matches. Using existing file.")
                needs_download = False
            else:
                print(f"❌ SHA256 mismatch. Removing corrupt file and re-downloading.")
                tar_path.unlink()

        if needs_download:
            print(f"⬇️  Downloading: {url}")
            def _progress_hook(block_num, block_size, total_size):
                downloaded = block_num * block_size
                percent = min(downloaded / total_size * 100, 100) if total_size > 0 else 0
                bar_len = 40
                filled_len = int(bar_len * percent // 100)
                bar = '=' * filled_len + '-' * (bar_len - filled_len)
                print(f"\r    [{bar}] {percent:5.1f}% ({downloaded // (1024*1024)}MB/{total_size // (1024*1024)}MB)", end='', flush=True)
                if downloaded >= total_size:
                    print()  # newline after done
            urllib.request.urlretrieve(url, tar_path, reporthook=_progress_hook)

            print(f"✅ Verifying SHA256 after download...")
            actual_sha = self._compute_sha256(tar_path)
            assert actual_sha == expected_sha256, f"SHA mismatch for {tar_path.name}"

        return tar_path

    def _extract_if_needed(self, tar_path):
        extract_dir = self.cache_dir / tar_path.stem.replace(".tar", "")
        if not extract_dir.exists():
            print(f"📦 Extracting {tar_path.name}")
            with tarfile.open(tar_path, "r:gz") as tar:
                tar.extractall(path=self.cache_dir)
        return extract_dir

    def _download_and_extract_one(self, subset: str):
        for dist in self.distributions:
            if subset == dist["name"]:
                filename = dist["name"] + ".tar.gz" if not dist["name"].endswith(".tar.gz") else dist["name"]
                tar_path = self.cache_dir / filename
                tar_path = self._download_file(dist["contentUrl"], tar_path, dist["sha256"])
                extract_dir = self._extract_if_needed(tar_path)
                return extract_dir
        raise ValueError(f"Subset '{subset}' not found in metadata.")

    def _matching_subsets(self, prefix: str):
        return sorted([dist["name"] for dist in self.distributions if dist["name"].startswith(f"IISc_RESPIN_{prefix}_")])

    def load(self, split: str) -> dict:
        all_data = {}

        # Full category: train, dev, test
        if split in {"train", "dev", "test"}:
            subsets = self._matching_subsets(split)
            print(f"🔍 Found {len(subsets)} '{split}' subsets: {[s.split('_')[-1] for s in subsets]}")

        # Language-wise group e.g. train_bh → all Bhojpuri train subsets
        elif split.startswith("train_") and len(split.split("_")) == 2:
            lang = split.split("_")[1]
            subsets = [
                dist["name"] for dist in self.distributions
                if dist["name"].startswith(f"IISc_RESPIN_train_{lang}_")
            ]
            if not subsets:
                raise ValueError(f"No train subsets found for language '{lang}'")
            print(f"🔍 Found {len(subsets)} training subsets for language '{lang}'")

        # Slab-wise group e.g. train_clean → all clean train subsets
        elif split.startswith("train_") and len(split.split("_")) == 2:
            slab = split.split("_")[1]
            subsets = [
                dist["name"] for dist in self.distributions
                if dist["name"].startswith("IISc_RESPIN_train_") and dist["name"].endswith(f"_{slab}")
            ]
            if not subsets:
                raise ValueError(f"No training subsets found for slab '{slab}'")
            print(f"🔍 Found {len(subsets)} training subsets for slab '{slab}'")

        # Exact match like dev_bn or train_ch_clean
        else:
            subsets = [dist["name"] for dist in self.distributions if dist["name"].endswith(split)]
            if not subsets:
                raise ValueError(f"No matching subset found for split '{split}'")
            print(f"🔍 Found 1 subset for '{split}'")

        for subset_name in subsets:
            print(f"\n📥 Processing subset: {subset_name}")
            extracted_folder = self._download_and_extract_one(subset_name)

            suffix = "_".join(extracted_folder.name.split("_")[2:])
            meta_path = extracted_folder / f"meta_{suffix}.json"
            print(f"📂 Loading metadata from {meta_path}")
            if not meta_path.exists():
                raise FileNotFoundError(f"Meta file not found: {meta_path}")

            with open(meta_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            for key, item in data.items():
                item["wav_path"] = os.path.join(extracted_folder, item["wav_path"])
                all_data[key] = item

            print(f"✅ Loaded {len(data)} records from {meta_path}")

        return all_data

