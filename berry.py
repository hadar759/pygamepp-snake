import random
from typing import Optional

import pygame

from snake_grid import SnakeGrid
from pygamepp.grid_game_object import GridGameObject


class Berry(GridGameObject):
    def __init__(self, berry_sprite: pygame.sprite, grid: SnakeGrid, block_size):
        berry_position = self.generate_position(grid, block_size)
        print(berry_position)
        super().__init__(berry_sprite, berry_position, block_size)

    def generate_position(self, grid, block_size: Optional[int] = None):
        if not block_size:
            block_size = self.block_size
        position = [[[y.y // block_size, y.x // block_size] for y in x if not y.occupied] for x in grid.blocks]
        ret_pos = random.choice(random.choice(position))
        return [ret_pos]