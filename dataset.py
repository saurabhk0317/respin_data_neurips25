import os
import tarfile
import datasets
import requests

_CITATION = """\
Add your dataset citation here.
"""

_DESCRIPTION = """\
RESPIN multilingual dataset for machine translation tasks.
"""

_HOMEPAGE = "https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/"

LANGUAGE_CODES = {
    "bh": "bhojpuri",
    "bn": "bengali",
    "ch": "chhattisgarhi",
    "hi": "hindi",
    "kn": "kannada",
    "mg": "magahi",
    "mr": "marathi",
    "mt": "maithili",
    "te": "telugu"
}

SPLIT_FILES = {
    "train_small": "IISc_RESPIN_train_small_{}.tar.gz",
    "train_clean": "IISc_RESPIN_train_clean_{}.tar.gz",
    "dev": "IISc_RESPIN_dev_{}.tar.gz"
}

SPLIT_NAME_MAP = {
    "train.tsv": datasets.Split.TRAIN,
    "dev.tsv": datasets.Split.VALIDATION,
    "test.tsv": datasets.Split.TEST,
}

class RespinConfig(datasets.BuilderConfig):
    def __init__(self, language_code, split, **kwargs):
        super().__init__(**kwargs)
        self.language_code = language_code
        self.language = LANGUAGE_CODES[language_code]
        self.split = split

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
                "source": datasets.Value("string"),
                "target": datasets.Value("string"),
            }),
            supervised_keys=("source", "target"),
            homepage=_HOMEPAGE,
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager):
        lang_code = self.config.language_code
        lang = self.config.language
        split = self.config.split

        url = f"{_HOMEPAGE}{lang}/{SPLIT_FILES[split].format(lang_code)}"
        filename = os.path.basename(url)
        cache_dir = dl_manager.download_config.cache_dir
        tar_path = os.path.join(cache_dir, filename)
        extract_path = os.path.join(cache_dir, filename.replace(".tar.gz", ""))

        os.makedirs(cache_dir, exist_ok=True)

        if not os.path.exists(tar_path):
            print(f"Downloading from {url} ...")
            response = requests.get(url, stream=True)
            if response.status_code != 200:
                raise RuntimeError(f"Download failed: HTTP {response.status_code}")
            with open(tar_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=1024 * 1024):
                    f.write(chunk)

        if not os.path.exists(extract_path):
            print(f"Extracting to {extract_path} ...")
            with tarfile.open(tar_path, "r:gz") as tar:
                tar.extractall(path=extract_path)

        splits = []
        for fname in os.listdir(extract_path):
            if fname.lower() in SPLIT_NAME_MAP:
                split_type = SPLIT_NAME_MAP[fname.lower()]
                splits.append(
                    datasets.SplitGenerator(
                        name=split_type,
                        gen_kwargs={"filepath": os.path.join(extract_path, fname)},
                    )
                )

        return splits

    def _generate_examples(self, filepath):
        with open(filepath, encoding="utf-8") as f:
            for idx, line in enumerate(f):
                parts = line.strip().split("\t")
                if len(parts) == 2:
                    source, target = parts
                    yield idx, {"source": source, "target": target}
