from typing import Optional

import pygame
from pygame import USEREVENT

from pygamepp.game import Game
from snake import Snake
from berry import Berry
from snake_grid import SnakeGrid


class SnakeGame(Game):
    BLOCK_SIZE = 60
    MOVE_TIMER = 200
    MOVE_EVENT_CODE = USEREVENT + 1
    RIGHT_BORDER = 15
    LOWER_BORDER = 17

    def __init__(self,
                 width: int,
                 height: int,
                 refresh_rate: int = 60,
                 background_path: Optional[str] = None):
        super().__init__(width, height, refresh_rate, background_path)
        self.snake_grid = SnakeGrid()
        snake_sprite = pygame.image.load(r"./resources/snake_sprite.png")
        berry_sprite = pygame.image.load(r"./resources/berry_sprite.png")
        self.snake = Snake(snake_sprite, self.snake_grid, self.BLOCK_SIZE)
        self.game_objects.append(self.snake)
        self.berry = Berry(berry_sprite, self.snake_grid, self.BLOCK_SIZE)
        self.game_objects.append(self.berry)
        self.direction = "right"

    def run(self):
        self.create_timer(self.MOVE_EVENT_CODE, self.MOVE_TIMER)
        self.set_event_handler(self.MOVE_EVENT_CODE, self.move)
        self.set_event_handler(pygame.KEYDOWN, self.change_direction)
        self.running = True
        self.snake_grid.display_borders(self.screen)
        super().run()

    def end_of_loop(self):
        self.occupy_snake()
        berry_pos = self.berry.position[0]
        snake_head = self.snake.position[0]
        if snake_head == tuple(berry_pos):
            self.berry_eaten()
        elif snake_head in self.snake.position[1:]:
            self.game_over()

    def occupy_snake(self):
        for pos in self.snake.position:
            self.snake_grid.occupy_block(pos)

    def berry_eaten(self):
        last_pos = self.snake.position[-1]
        self.snake.position.append(last_pos)
        self.berry.position = self.berry.generate_position(self.snake_grid)

    def change_direction(self, event):
        if event.key == pygame.K_RIGHT:
            self.direction = "right"
        elif event.key == pygame.K_LEFT:
            self.direction = "left"
        elif event.key == pygame.K_UP:
            self.direction = "up"
        elif event.key == pygame.K_DOWN:
            self.direction = "down"

    def move(self):
        if self.direction == "right":
            self.snake.move_right()
        elif self.direction == "left":
            self.snake.move_left()
        elif self.direction == "up":
            self.snake.move_up()
        elif self.direction == "down":
            self.snake.move_down()
        self.snake_grid.reset_screen(self.screen)
        snake_head = self.snake.position[0]
        if snake_head[1] < 0 or snake_head[1] > self.RIGHT_BORDER or snake_head[0] < 0 or snake_head[0] > self.LOWER_BORDER:
            self.quit()

    def game_over(self):
        pygame.time.wait(5000)
        pygame.quit()