class MullLayer:
    def __init__(self) -> None:
        self.x = None
        self.y = None

    def forward(self, x, y):
        self.x = x
        self.y = y
        return x * y
    
    def backward(self, d_out):
        dx = d_out * self.y
        dy = d_out * self.x
        return dx, dy

class AddLayer:
    def __init__(self) -> None:
        pass

    def forward(self, x, y):
        self.x = x
        self.y = y
        return x + y
    
    def backward(self, d_out):
        return d_out, d_out # dx, dy: z = x + y, z'(x) = 1, z'(y) = 1