#!/usr/bin/env python3
"""Main entry point for the Snake game."""

import curses
import time
from typing import Optional

from snake.snake import Snake, Direction
from snake.food import Food
from snake.input_handler import InputHandler
from snake.renderer import Renderer


class Game:
    def __init__(self, stdscr: curses.window) -> None:
        self.stdscr = stdscr
        self.renderer = Renderer(stdscr)
        self.input_handler = InputHandler()
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.difficulty = "MEDIUM"
        self.game_over = False
        self._init_difficulty()

    def _init_difficulty(self) -> None:
        difficulty_speeds = {
            "EASY": 150,
            "MEDIUM": 100,
            "HARD": 50,
        }
        self.stdscr.timeout(difficulty_speeds[self.difficulty])

    def _handle_input(self) -> None:
        key = self.stdscr.getch()
        if key != -1:
            self.input_handler.process_key(key)
            new_direction = self.input_handler.get_direction()
            self.snake.set_direction(Direction[new_direction])

    def _update_game_state(self) -> None:
        if self.game_over:
            return

        self.snake.move()
        head = self.snake.get_head_position()

        if self._check_collision(head):
            self.game_over = True
            return

        if head == self.food.get_position():
            self.snake.grow()
            self.score += 1
            self.food.spawn(*self._get_available_area(), self.snake.get_body_positions())

    def _check_collision(self, head: tuple[int, int]) -> bool:
        width, height = self.renderer.get_board_dimensions()
        if head[0] <= 0 or head[0] >= width - 1 or head[1] <= 0 or head[1] >= height - 1:
            return True
        return self.snake.check_self_collision()

    def _get_available_area(self) -> tuple[int, int]:
        width, height = self.renderer.get_board_dimensions()
        return width - 2, height - 2

    def _draw(self) -> None:
        self.renderer.render(
            self.snake,
            self.food,
            self.score,
            self.difficulty,
            self.game_over
        )

    def run(self) -> None:
        self.food.spawn(*self._get_available_area(), self.snake.get_body_positions())

        while not self.game_over:
            self._handle_input()
            self._update_game_state()
            self._draw()
            time.sleep(0.05)


def main(stdscr: curses.window) -> None:
    game = Game(stdscr)
    game.run()


if __name__ == "__main__":
    curses.wrapper(main)
