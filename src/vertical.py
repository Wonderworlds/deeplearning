import matplotlib.pyplot as plt
import numpy as np
import nnfs
from nnfs.datasets import vertical_data
from layer_dense import Layer_Dense
from layer_activation import ReLU_activation, SoftMax_activation
from loss import Loss_CategoricalCrossEntropy

nnfs.init()

X, y = vertical_data(samples=100, classes=3)

dense1 = Layer_Dense(2, 3)

activation1 = ReLU_activation()

dense2 = Layer_Dense(3, 3)

activation2 = SoftMax_activation()

loss_function = Loss_CategoricalCrossEntropy()

lowest_loss = 999999999
best_dense1_weights = dense1.weights.copy()
best_dense1_biases = dense1.biases.copy()
best_dense2_weights = dense2.weights.copy()
best_dense2_biases = dense2.biases.copy()

for iteration in range(100000):
    dense1.weights += 0.05 * np.random.randn(2, 3)
    dense1.biases += 0.05 * np.random.randn(1, 3)
    dense2.weights += 0.05 * np.random.randn(3, 3)
    dense2.biases += 0.05 * np.random.randn(1, 3)

    dense1.forward(X)
    activation1.forward(dense1.output)
    dense2.forward(activation1.output)
    activation2.forward(dense2.output)

    loss = loss_function.calculate(activation2.output, y)

    predictions = np.argmax(activation2.output, axis=1)
    accuracy = np.mean(predictions == y)

    if loss < lowest_loss:
        print(
            "New set of weights found, iteration:",
            iteration,
            "loss:",
            loss,
            "acc:",
            accuracy,
        )
        best_dense1_weights = dense1.weights.copy()
        best_dense1_biases = dense1.biases.copy()
        best_dense2_weights = dense2.weights.copy()
        best_dense2_biases = dense2.biases.copy()
        lowest_loss = loss
    else:
        dense1.weights = best_dense1_weights.copy()
        dense1.biases = best_dense1_biases.copy()
        dense2.weights = best_dense2_weights.copy()
        dense2.biases = best_dense2_biases.copy()


# plt.scatter(X[:, 0], X[:, 1], c=y, cmap="brg")
# plt.show()
