from matplotlib import pyplot as plt
from dataset.train_data import TrainData

trainData = TrainData()

class Visual:
    def __init__(self) -> None:
        figure_size = plt.figure(figsize=(10, 10))

    def visual_show(self) -> None:
        for images, labels in trainData.take(1):
            