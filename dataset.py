import os
import tarfile
import datasets
import requests
import json
from tqdm import tqdm

_CITATION = """Add your dataset citation here."""
_DESCRIPTION = """RESPIN multilingual dataset with audio and metadata."""
_HOMEPAGE_TEMPLATE = "https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/{}/"

LANGUAGE_CODES = {
    "bh": "bhojpuri", "bn": "bengali", "ch": "chhattisgarhi", "hi": "hindi",
    "kn": "kannada", "mg": "magahi", "mr": "marathi", "mt": "maithili", "te": "telugu"
}

SPLIT_FILES = {
    "train_small": "IISc_RESPIN_train_small_{}.tar.gz",
    "train_clean": "IISc_RESPIN_train_clean_{}.tar.gz",
    "train_seminoisy": "IISc_RESPIN_train_seminoisy_{}.tar.gz",
    "train_noisy": "IISc_RESPIN_train_noisy_{}.tar.gz",
    "dev": "IISc_RESPIN_dev_{}.tar.gz",
    "lexicon": "IISc_RESPIN_lexicon_{}.txt"  # Not a tar file
}

class RespinConfig(datasets.BuilderConfig):
    def __init__(self, language_code, split, delete_tar_after_extract=True, **kwargs):
        super().__init__(**kwargs)
        self.language_code = language_code
        self.language = LANGUAGE_CODES[language_code]
        self.split = split
        self.delete_tar_after_extract = delete_tar_after_extract

class RespinDataset(datasets.GeneratorBasedBuilder):
    BUILDER_CONFIGS = [
        RespinConfig(name=f"{code}_{split}", version=datasets.Version("1.0.0"),
                     description=f"RESPIN dataset for {LANGUAGE_CODES[code]} - {split}",
                     language_code=code, split=split)
        for code in LANGUAGE_CODES
        for split in SPLIT_FILES
    ]

    def _info(self):
        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=datasets.Features({
                "utterance_id": datasets.Value("string"),
                "text": datasets.Value("string"),
                "wav_path": datasets.Value("string"),
                "dialect": datasets.Value("string"),
                "gender": datasets.Value("string"),
                "age_group": datasets.Value("string"),
                "domain": datasets.Value("string"),
                "speaker_id": datasets.Value("string"),
                "pincode": datasets.Value("string"),
                "duration": datasets.Value("float"),
            }),
            supervised_keys=None,
            homepage=_HOMEPAGE_TEMPLATE.format("{language}"),
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager):
        lang_code = self.config.language_code
        lang_full = self.config.language
        split = self.config.split
        delete_tar = self.config.delete_tar_after_extract

        filename = SPLIT_FILES[split].format(lang_code)
        url = _HOMEPAGE_TEMPLATE.format(lang_full) + filename

        cache_dir = os.path.join(dl_manager.download_config.cache_dir, lang_code)
        os.makedirs(cache_dir, exist_ok=True)
        file_path = os.path.join(cache_dir, filename)

        # Handle lexicon: download and return nothing
        if split == "lexicon":
            if not os.path.exists(file_path):
                print(f"Downloading {filename} from {url} ...", flush=True)
                response = requests.get(url, stream=True)
                if response.status_code != 200:
                    raise RuntimeError(f"Download failed: HTTP {response.status_code}")
                total = int(response.headers.get("content-length", 0))
                with open(file_path, "wb") as f, tqdm(
                    desc=f"Downloading {filename}",
                    total=total,
                    unit='B',
                    unit_scale=True,
                    unit_divisor=1024,
                ) as bar:
                    for chunk in response.iter_content(1024 * 1024):
                        if chunk:
                            f.write(chunk)
                            bar.update(len(chunk))
            print(f"Lexicon file saved at: {file_path}", flush=True)
            return []

        # Proceed with tar download/extraction for other splits
        tar_path = file_path
        extract_dir = os.path.join(cache_dir, f"IISc_RESPIN_{split}_{lang_code}")
        meta_path = os.path.join(extract_dir, f"meta_{split}_{lang_code}.json")

        # Download tar if not present
        if not os.path.exists(tar_path):
            print(f"Downloading {filename} from {url} ...", flush=True)
            response = requests.get(url, stream=True)
            if response.status_code != 200:
                raise RuntimeError(f"Download failed: HTTP {response.status_code}")
            total = int(response.headers.get("content-length", 0))
            with open(tar_path, "wb") as f, tqdm(
                desc=f"Downloading {filename}",
                total=total,
                unit='B',
                unit_scale=True,
                unit_divisor=1024,
            ) as bar:
                for chunk in response.iter_content(1024 * 1024):
                    if chunk:
                        f.write(chunk)
                        bar.update(len(chunk))

        # Extract if needed
        if not os.path.exists(meta_path):
            print(f"Extracting {tar_path} to {cache_dir} ...", flush=True)
            with tarfile.open(tar_path, "r:gz") as tar:
                tar.extractall(path=cache_dir)

        # Optionally delete tar
        if delete_tar and os.path.exists(tar_path):
            print(f"Deleting tar file: {tar_path}", flush=True)
            os.remove(tar_path)

        if not os.path.exists(meta_path):
            raise FileNotFoundError(f"Expected meta file not found: {meta_path}")

        return [
            datasets.SplitGenerator(
                name=datasets.Split.TRAIN if "train" in split else datasets.Split.VALIDATION,
                gen_kwargs={"meta_path": meta_path, "extract_dir": extract_dir},
            )
        ]

    def _generate_examples(self, meta_path, extract_dir):
        with open(meta_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        for idx, (utt_id, item) in enumerate(data.items()):
            wav_rel_path = item.get("wav_path", "")
            wav_abs_path = os.path.join(extract_dir, wav_rel_path)
            yield idx, {
                "utterance_id": utt_id,
                "text": item.get("text", ""),
                "wav_path": wav_abs_path,
                "dialect": item.get("dialect", ""),
                "gender": item.get("gender", ""),
                "age_group": item.get("age_group", ""),
                "domain": item.get("domain", ""),
                "speaker_id": item.get("speaker_id", ""),
                "pincode": item.get("pincode", ""),
                "duration": float(item.get("duration", 0.0)),
            }
