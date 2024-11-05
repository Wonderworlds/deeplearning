import numpy as np
import nnfs
import matplotlib.pyplot as plt
from nnfs.datasets import spiral_data
from layer_dense import Layer_Dense
from layer_activation import ReLU_activation, SoftMax_activation
from loss import Loss_CategoricalCrossEntropy

nnfs.init()


def accuracy(inputs: np.array, labels: np.array):
    predictions = np.argmax(inputs, axis=1)

    if len(labels.shape) == 2:
        labels = np.argmax(labels, axis=1)
    accuracy = np.mean(predictions == labels)

    print("acc:", accuracy)


x, y = spiral_data(samples=100, classes=3)

dense1 = Layer_Dense(2, 3)

activation1 = ReLU_activation()

dense2 = Layer_Dense(3, 3)

activation2 = SoftMax_activation()

dense1.forward(x)
activation1.forward(dense1.output)

dense2.forward(activation1.output)
activation2.forward(dense2.output)

print(activation2.output[:5])

loss_function = Loss_CategoricalCrossEntropy()
loss = loss_function.calculate(activation2.output, y)

print("loss:", loss)

accuracy(activation2.output, y)


# plt.scatter(x[:, 0], x[:, 1], c=y, cmap="brg")
# plt.show()
