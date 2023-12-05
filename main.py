import matplotlib.pyplot as plt
import numpy as np
import PIL
import tensorflow as tf

from tensorflow import keras
from keras import layers
from keras.models import Sequential

from core.data import Data
from dataset.train_data import TrainData
from dataset.validate_data import ValidateData


def main() -> None:
    data = Data()
    image_counter = len(list(data.data_dir.glob('*/*.jpg')))
    print(image_counter)

    trainData = TrainData()
    valData = ValidateData()

if __name__ == "__main__":
    main()