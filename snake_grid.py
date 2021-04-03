import pygame

from pygamepp.grid import Grid
from colors import Colors


class SnakeGrid(Grid):
    def __init__(self):
        super().__init__(17, 15, 60)

    def display_borders(self, screen: pygame.Surface):
        block_size = 60
        for row in self.blocks:
            for block in row:
                pygame.draw.line(screen, Colors.GREY,
                                 (block.x, block.y), (block.x + 10,
                                                      block.y))
                pygame.draw.line(screen, Colors.DARK_GREY,
                                 (block.x + 10, block.y),
                                 (block.x + block_size - 10, block.y))
                pygame.draw.line(screen, Colors.GREY,
                                 (block.x, block.y), (block.x,
                                                      block.y + 10))
                pygame.draw.line(screen, Colors.DARK_GREY,
                                 (block.x, block.y + 10),
                                 (block.x, block.y + block_size - 10))
                pygame.draw.line(screen, Colors.GREY,
                                 (block.x + block_size, block.y),
                                 (block.x + block_size - 10, block.y))
                pygame.draw.line(screen, Colors.GREY,
                                 (block.x + block_size, block.y),
                                 (block.x + block_size, block.y + 10))
                pygame.draw.line(screen, Colors.GREY,
                                 (block.x + block_size,
                                  block.y + block_size)
                                 , (block.x + block_size - 10,
                                    block.y + block_size))
                pygame.draw.line(screen, Colors.GREY,
                                 (block.x + block_size,
                                  block.y + block_size),
                                 (block.x + block_size,
                                  block.y + block_size - 10))
                pygame.draw.line(screen, Colors.GREY,
                                 (block.x, block.y + block_size),
                                 (block.x + 10, block.y + block_size))
                pygame.draw.line(screen, Colors.GREY,
                                 (block.x, block.y + block_size),
                                 (block.x, block.y + block_size - 10))
                pygame.draw.line(screen, Colors.DARK_GREY,
                                 (block.x + 10, block.y + block_size),
                                 (block.x + block_size - 10,
                                  block.y + block_size))

    def reset_screen(self, screen: pygame.Surface):
        screen.fill(Colors.BLACK)
        self.display_borders(screen)
