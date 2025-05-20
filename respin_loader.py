import os
import json
import hashlib
import tarfile
import urllib.request
from pathlib import Path

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

    def _download_and_extract(self, subset: str):
        for dist in self.distributions:
            if subset in dist["name"]:
                url = dist["contentUrl"]
                sha256 = dist["sha256"]
                filename = dist["name"] + ".tar.gz" if not dist["name"].endswith(".tar.gz") else dist["name"]
                tar_path = self.cache_dir / filename

                if not tar_path.exists():
                    self.cache_dir.mkdir(parents=True, exist_ok=True)
                    print(f"⬇️  Downloading: {url}")
                    def _progress_hook(block_num, block_size, total_size):
                        downloaded = block_num * block_size
                        percent = min(downloaded / total_size * 100, 100) if total_size > 0 else 0
                        bar_len = 40
                        filled_len = int(bar_len * percent // 100)
                        bar = '=' * filled_len + '-' * (bar_len - filled_len)
                        print(f"\r    [{bar}] {percent:5.1f}% ({downloaded // (1024*1024)}MB/{total_size // (1024*1024)}MB)", end='', flush=True)
                        if downloaded >= total_size:
                            print()  # Newline after done

                    urllib.request.urlretrieve(url, tar_path, reporthook=_progress_hook)

                print(f"✅ Verifying SHA256...")
                actual_sha = self._compute_sha256(tar_path)
                assert actual_sha == sha256, f"SHA mismatch for {filename}"

                # Extract if not already extracted
                extracted_folder = self.cache_dir / filename.replace(".tar.gz", "")
                
                # print(f"📦 Checking extracted folder: {extracted_folder}")
                if not extracted_folder.exists():
                    print(f"📦 Extracting to {self.cache_dir}")
                    with tarfile.open(tar_path, "r:gz") as tar:
                        tar.extractall(path=self.cache_dir)

                return extracted_folder

        raise ValueError(f"Subset '{subset}' not found in metadata.")

    def load(self, split: str) -> dict:
        extracted_folder = self._download_and_extract(split)
        
        print(f"📂 Loading data from {extracted_folder}")
        
        suffix = "_".join(extracted_folder.name.split("/")[-1].split("_")[2:])
        meta_path = extracted_folder / f"meta_{suffix}.json"
        print(f"📂 Loading metadata from {meta_path}")
        
        if not meta_path.exists():
            raise FileNotFoundError(f"Meta file not found: {meta_path}")

        with open(meta_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            
        # Prepend extracted folder to each file wav_path
        for item in data.values():
            item["wav_path"] = os.path.join(extracted_folder, item["wav_path"])

        

        print(f"✅ Loaded {len(data)} records from {meta_path}")
        return data
