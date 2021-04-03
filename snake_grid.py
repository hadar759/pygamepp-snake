import pygame

from pygamepp.grid import Grid
from colors import Colors


class SnakeGrid(Grid):
    def __init__(self):
        super().__init__(17, 15, 60)
        self.block_size = 60

    def display_borders(self, screen: pygame.Surface):
        """Displays the border of every block in the grid"""
        for row in self.blocks:
            for block in row:
                x = block.x
                y = block.y

                self.draw_horizontal_line(x, y, screen)

                self.draw_vertical_line(
                    x + self.block_size, y + self.block_size, screen
                )

                # Draw the right line only if it's the first column,
                # performance sake as to not draw it many times over.
                if row[0] == block:
                    self.draw_vertical_line(x, y, screen)

    def draw_horizontal_line(self, x, y, screen):
        """Draws a horizontal block separator"""
        first_coords = [x, y]
        second_coords = [first_coords[0] + 10, first_coords[1]]
        pygame.draw.line(screen, Colors.GREY, first_coords, second_coords)

        first_coords, second_coords = second_coords, [
            first_coords[0] + self.block_size - 10,
            first_coords[1],
        ]
        pygame.draw.line(screen, Colors.DARK_GREY, first_coords, second_coords)

        first_coords = second_coords
        second_coords = [first_coords[0] + 10, first_coords[1]]
        pygame.draw.line(screen, Colors.GREY, first_coords, second_coords)

    def draw_vertical_line(self, x, y, screen):
        """Draws a vertical block separator"""
        first_coords = [x, y]
        second_coords = [first_coords[0], first_coords[1] + 10]
        pygame.draw.line(screen, Colors.GREY, first_coords, second_coords)

        first_coords, second_coords = second_coords, [
            first_coords[0],
            first_coords[1] + self.block_size - 10,
        ]
        pygame.draw.line(screen, Colors.DARK_GREY, first_coords, second_coords)

        first_coords = second_coords
        second_coords = [first_coords[0], first_coords[1] + 10]
        pygame.draw.line(screen, Colors.GREY, first_coords, second_coords)

    def reset_screen(self, screen: pygame.Surface):
        screen.fill(Colors.BLACK)
        self.display_borders(screen)
