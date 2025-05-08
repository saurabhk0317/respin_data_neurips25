import os
import datasets
import tarfile

_CITATION = """\
Add your dataset citation here.
"""

_DESCRIPTION = """\
RESPIN multilingual dataset for machine translation tasks.
"""

_HOMEPAGE = "https://objectstore.e2enetworks.net/respin-dataset-neurips/respin/"

# Mapping of language codes to full language names
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

# Available splits and their corresponding filenames
SPLIT_FILES = {
    "train_small": "IISc_RESPIN_train_small_{}.tar.gz",
    "train_clean": "IISc_RESPIN_train_clean_{}.tar.gz",
    "dev": "IISc_RESPIN_dev_{}.tar.gz"
}

class RespinConfig(datasets.BuilderConfig):
    def __init__(self, language_code, **kwargs):
        super().__init__(**kwargs)
        self.language_code = language_code
        self.language = LANGUAGE_CODES[language_code]

class RespinDataset(datasets.GeneratorBasedBuilder):
    BUILDER_CONFIGS = [
        RespinConfig(name=code, version=datasets.Version("1.0.0"), description=f"RESPIN dataset for {LANGUAGE_CODES[code]}", language_code=code)
        for code in LANGUAGE_CODES
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

        urls = {
            split: f"{_HOMEPAGE}{lang}/{filename.format(lang_code)}"
            for split, filename in SPLIT_FILES.items()
        }

        downloaded_files = dl_manager.download_and_extract(urls)

        return [
            datasets.SplitGenerator(name=datasets.Split.TRAIN, gen_kwargs={"filepath": downloaded_files["train_small"]}),
            datasets.SplitGenerator(name=datasets.Split.VALIDATION, gen_kwargs={"filepath": downloaded_files["dev"]}),
            datasets.SplitGenerator(name=datasets.Split.TEST, gen_kwargs={"filepath": downloaded_files["train_clean"]}),
        ]

    def _generate_examples(self, filepath):
        id_ = 0
        for root, _, files in os.walk(filepath):
            for file in files:
                if file.endswith(".tsv"):
                    with open(os.path.join(root, file), encoding="utf-8") as f:
                        for line in f:
                            parts = line.strip().split("\t")
                            if len(parts) == 2:
                                source, target = parts
                                yield id_, {"source": source, "target": target}
                                id_ += 1
