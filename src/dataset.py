import tensorflow as tf
import tensorflow_datasets as tfds

class Dataset():
    
    def __init__(self) -> None:
        self.sample = self._load_sample()

    def _load_sample(self) -> tf.data.Dataset:
        sample = tfds.load("rock_paper_scissors", split="train", try_gcs=True)
        assert isinstance(self.sample, tf.data.Dataset)
        return sample