import keras

from core.data import Data

batch_size = 32
img_height = 180
img_width = 180

data = Data()

class TrainData:
    def __init__(self) -> None:
        self.train_ds = keras.utils.image_dataset_from_directory(
        data.data_dir,
        validation_split=0.2,
        subset="training",
        seed=123,
        image_size=(img_height, img_width),
        batch_size=(batch_size)
    )
        

        
    