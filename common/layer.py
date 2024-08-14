import numpy as np

class Relu:
    def __init__(self) -> None:
        self.mask = None

    # @param x numpy array
    def forward(self, x):
        self.mask = (x <= 0)
        out = x.copy()
        out[self.mask] = 0 # 0以下の要素を0にする
        return out
    
    def backward(self, d_out):
        d_out[self.mask] = 0 # 0以下の要素の微分した値を0とする
        dx = d_out * 1 # x > 0のとき f(x) = x より f'(x) = 1 よって、 * 1をする。
        return dx

class Sigmoid:
    def __init__(self) -> None:
        self.out = None

    def forward(self, x):
        out = 1 / (1 + np.exp(-x))
        self.out = out
        return out
    
    def backward(self, d_out):
        return d_out * (1.0 - self.out) * self.out