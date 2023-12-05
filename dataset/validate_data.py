import keras

from core.data import Data

batch_size = 32
img_height = 180
img_width = 180

data = Data()

class ValidateData:
    def __init__(self) -> None:
        self.val_ds = keras.utils.image_dataset_from_directory(
        data.data_dir,
        validation_split=0.2,
        subset="validation",
        seed=123,
        image_size=(img_height, img_width),
        batch_size=(batch_size)
    )