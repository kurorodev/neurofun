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
from visualize.visual import Visual

def main() -> None:
    data = Data()
    image_counter = len(list(data.data_dir.glob('*/*.jpg')))
    print(image_counter)

    trainData = TrainData()
    valData = ValidateData()
    visual = Visual()

    #visual.visual_show()

    for image_batch, label_batch in trainData.train_ds:
        print(image_batch.shape)
        print(label_batch.shape)
        break
        
if __name__ == "__main__":
    main()