import pygame

from snake_grid import SnakeGrid
from pygamepp.grid_game_object import GridGameObject


class Snake(GridGameObject):
    def __init__(self, sprite: pygame.sprite, grid: SnakeGrid, block_size):
        snake_head = (grid.width // 2, grid.height // 2)
        positions = [snake_head,  # Snake head
                          (snake_head[0], snake_head[1] - 1),     # Rest of the body
                          (snake_head[0], snake_head[1] - 2)]
        super().__init__(sprite, positions, block_size)

    def move_right(self):
        snake_head = self.position[0]
        self.position.insert(0, (snake_head[0], snake_head[1] + 1))
        self.position.pop()

    def move_left(self):
        snake_head = self.position[0]
        self.position.insert(0, (snake_head[0], snake_head[1] - 1))
        self.position.pop()

    def move_up(self):
        snake_head = self.position[0]
        self.position.insert(0, (snake_head[0] - 1, snake_head[1]))
        self.position.pop()

    def move_down(self):
        snake_head = self.position[0]
        self.position.insert(0, (snake_head[0] + 1, snake_head[1]))
        self.position.pop()

