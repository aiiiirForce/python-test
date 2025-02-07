class Shape:
    def __init__(self, color):
        self.color = color
        self.position = (3, 0)  # Starting position
        self.rotation = 0

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.shape)

    def move(self, dx, dy):
        self.position = (self.position[0] + dx, self.position[1] + dy)

class IShape(Shape):
    shape = [
        [[1, 1, 1, 1]],  # Horizontal
        [[1], 
         [1], 
         [1], 
         [1]]  # Vertical
    ]

    def __init__(self):
        super().__init__(color='cyan')

class JShape(Shape):
    shape = [
        [[0, 0, 1],
         [1, 1, 1]],  # Normal
        [[1, 0, 0],
         [1, 1, 1]],  # Rotated
        [[1, 1, 1],
         [0, 0, 1]],  # Upside down
        [[1, 1],
         [1, 0],
         [1, 0]]  # Flipped
    ]

    def __init__(self):
        super().__init__(color='blue')

class LShape(Shape):
    shape = [
        [[1, 0, 0],
         [1, 1, 1]],  # Normal
        [[1, 1],
         [1, 0],
         [1, 0]],  # Flipped
        [[1, 1, 1],
         [0, 0, 1]],  # Upside down
        [[0, 0, 1],
         [0, 0, 1],
         [1, 1]]  # Rotated
    ]

    def __init__(self):
        super().__init__(color='orange')

class OShape(Shape):
    shape = [
        [[1, 1],
         [1, 1]]  # Square
    ]

    def __init__(self):
        super().__init__(color='yellow')

class SShape(Shape):
    shape = [
        [[0, 1, 1],
         [1, 1, 0]],  # Normal
        [[1, 0],
         [1, 1],
         [0, 1]]  # Rotated
    ]

    def __init__(self):
        super().__init__(color='green')

class TShape(Shape):
    shape = [
        [[0, 1, 0],
         [1, 1, 1]],  # Normal
        [[1, 0],
         [1, 1],
         [1, 0]],  # Rotated
        [[1, 1, 1],
         [0, 1, 0]],  # Upside down
        [[0, 1],
         [1, 1],
         [0, 1]]  # Flipped
    ]

    def __init__(self):
        super().__init__(color='purple')

class ZShape(Shape):
    shape = [
        [[1, 1, 0],
         [0, 1, 1]],  # Normal
        [[0, 1],
         [1, 1],
         [1, 0]]  # Rotated
    ]

    def __init__(self):
        super().__init__(color='red')