import tensorflow as tf
import tensorflow_datasets as tfds

class Dataset():
    """Handles the datasets."""
    def __init__(self) -> None:
        self.train_sample, self.test_sample = self._load_sample()
        print(f"Sample {self.test_sample}, {self.test_sample}")

    def _load_sample(self) -> tf.data.Dataset:
        """Return train and test data samples."""
        train_sample, test_sample = tfds.load(
            "rock_paper_scissors",
            split=["train", "test[:30%]"],
            data_dir="dataset",
            shuffle_files=True,
            as_supervised=True,
            try_gcs=True)
        assert isinstance(train_sample, tf.data.Dataset)
        assert isinstance(test_sample, tf.data.Dataset)
        return train_sample, test_sample
