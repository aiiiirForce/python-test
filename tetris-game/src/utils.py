import random

def random_shape():
    shapes = ['I', 'O', 'T', 'S', 'Z', 'J', 'L']
    return random.choice(shapes)

def check_boundary(shape, offset, board):
    for x, y in shape:
        if x + offset[0] < 0 or x + offset[0] >= len(board[0]) or y + offset[1] >= len(board):
            return False
    return True

def check_collision(shape, offset, board):
    for x, y in shape:
        if y + offset[1] >= 0 and board[y + offset[1]][x + offset[0]] != 0:
            return True
    return False