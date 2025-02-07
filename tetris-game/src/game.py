import pygame
import random
import os
from shapes import IShape, JShape, LShape, OShape, SShape, TShape, ZShape

class Game:
    SHAPES = [IShape, JShape, LShape, OShape, SShape, TShape, ZShape]

    def __init__(self, width=10, height=20):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.current_shape = None
        self.next_shape = None
        self.score = 0
        self.screen = pygame.display.get_surface()
        self.new_shape()
        self.drop_time = 0
        self.drop_interval = 500  # 下落间隔时间（毫秒）
        self.game_over = False
        self.keys = {pygame.K_LEFT: False, pygame.K_RIGHT: False, pygame.K_DOWN: False}
        self.font_path = os.path.join(os.path.dirname(__file__), 'SimHei.ttf')

    def new_shape(self):
        self.current_shape = random.choice(self.SHAPES)()
        if self.check_collision():
            self.game_over = True

    def rotate_shape(self):
        self.current_shape.rotate()
        if self.check_collision():
            self.current_shape.rotate()
            self.current_shape.rotate()
            self.current_shape.rotate()

    def move_shape(self, dx, dy):
        self.current_shape.move(dx, dy)
        if self.check_collision():
            self.current_shape.move(-dx, -dy)
            if dy > 0:  # If the collision happened while moving down
                self.fix_shape()
                self.new_shape()

    def drop_shape(self):
        while not self.check_collision():
            self.current_shape.move(0, 1)
        self.current_shape.move(0, -1)
        self.fix_shape()
        self.new_shape()

    def check_collision(self):
        shape_matrix = self.current_shape.shape[self.current_shape.rotation]
        for y, row in enumerate(shape_matrix):
            for x, cell in enumerate(row):
                if cell:
                    new_x = self.current_shape.position[0] + x
                    new_y = self.current_shape.position[1] + y
                    if new_x < 0 or new_x >= self.width or new_y >= self.height or self.board[new_y][new_x]:
                        return True
        return False

    def fix_shape(self):
        shape_matrix = self.current_shape.shape[self.current_shape.rotation]
        for y, row in enumerate(shape_matrix):
            for x, cell in enumerate(row):
                if cell:
                    self.board[self.current_shape.position[1] + y][self.current_shape.position[0] + x] = 1
        self.clear_lines()

    def clear_lines(self):
        new_board = [row for row in self.board if any(cell == 0 for cell in row)]
        lines_cleared = self.height - len(new_board)
        self.board = [[0] * self.width for _ in range(lines_cleared)] + new_board
        self.score += lines_cleared

    def update(self):
        if not self.game_over:
            current_time = pygame.time.get_ticks()
            if current_time - self.drop_time > self.drop_interval:
                self.move_shape(0, 1)
                self.drop_time = current_time

            if self.keys[pygame.K_LEFT]:
                self.move_shape(-1, 0)
            if self.keys[pygame.K_RIGHT]:
                self.move_shape(1, 0)
            if self.keys[pygame.K_DOWN]:
                self.move_shape(0, 1)

    def draw(self):
        self.screen.fill((0, 0, 0))
        
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] != 0:
                    pygame.draw.rect(self.screen, (255, 255, 255), (x * 30, y * 30, 30, 30))
        
        if self.current_shape:
            shape_matrix = self.current_shape.shape[self.current_shape.rotation]
            for y, row in enumerate(shape_matrix):
                for x, cell in enumerate(row):
                    if cell:
                        pygame.draw.rect(self.screen, (255, 255, 255), ((self.current_shape.position[0] + x) * 30, (self.current_shape.position[1] + y) * 30, 30, 30))

        if self.game_over:
            try:
                print(f"Font path: {self.font_path}")  # 打印字体路径
                font = pygame.font.SysFont('Arial', 55)  # 使用系统字体
                text = font.render("Game Over", True, (255, 0, 0))
                text_rect = text.get_rect(center=(self.width * 15, self.height * 15))  # 控制字体位置
                self.screen.blit(text, text_rect)
            except FileNotFoundError:
                print(f"Font file not found: {self.font_path}")

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN and not self.game_over:
            if event.key == pygame.K_LEFT:
                self.keys[pygame.K_LEFT] = True
            elif event.key == pygame.K_RIGHT:
                self.keys[pygame.K_RIGHT] = True
            elif event.key == pygame.K_DOWN:
                self.keys[pygame.K_DOWN] = True
            elif event.key == pygame.K_SPACE:
                self.rotate_shape()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.keys[pygame.K_LEFT] = False
            elif event.key == pygame.K_RIGHT:
                self.keys[pygame.K_RIGHT] = False
            elif event.key == pygame.K_DOWN:
                self.keys[pygame.K_DOWN] = False