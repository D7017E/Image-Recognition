import tensorflow as tf
import tensorflow_datasets as tfds

class Dataset():
    
    def __init__(self) -> None:
        self.sample = self._load_sample()
        print(f"")

    def _load_sample(self) -> tf.data.Dataset:
        sample = tfds.load("rock_paper_scissors", split="train", shuffle_files=True, as_supervised=True, try_gcs=True)
        assert isinstance(sample, tf.data.Dataset)
        return sample