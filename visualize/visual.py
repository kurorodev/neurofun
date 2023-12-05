from matplotlib import pyplot as plt
from dataset.train_data import TrainData
import numpy 

trainData = TrainData()

class Visual:
    def __init__(self) -> None:
        figure_size = plt.figure(figsize=(10, 10))

    def visual_show(self) -> None:
        for images in trainData.train_ds.take(1):
            for i in range(9):
                ax = plt.subplot(3, 3, i + 1)
                plt.imshow(images[i].numpy().astype("uint8"))
                plt.axis("off")