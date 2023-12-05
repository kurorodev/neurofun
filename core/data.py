import pathlib
import tensorflow as tf


class Data:
    def __init__(self) -> None:
        self.data_dir = tf.keras.utils.get_file(
            'flower_photos',
            origin='https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz',
            untar=True
        )
        self.data_dir = pathlib.Path(self.data_dir).with_suffix('')