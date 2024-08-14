import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    return np.array(x > 0, dtype=int)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(0, x)

def identity(x):
    return x

def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c)
    sum_exp_a = np.sum(exp_a)
    return exp_a / sum_exp_a

# x = np.arange(-5.0, 5.0, 0.1)
# y1 = step_function(x)
# y2 = sigmoid(x)

# plt.plot(x, y1, label = "step")
# plt.plot(x, y2, label = "sigmoid", linestyle = '--')
# plt.legend()
# plt.ylim(-0.1, 1.1)
# plt.show()
