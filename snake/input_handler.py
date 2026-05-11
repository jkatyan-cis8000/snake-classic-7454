import curses
from typing import Literal

Direction = Literal["UP", "DOWN", "LEFT", "RIGHT"]
Difficulty = Literal["EASY", "MEDIUM", "HARD"]


class InputHandler:
    def __init__(self) -> None:
        self._direction: Direction = "UP"
        self._difficulty: Difficulty = "MEDIUM"

    def get_direction(self) -> Direction:
        return self._direction

    def get_difficulty(self) -> Difficulty:
        return self._difficulty

    def change_direction(self, new_direction: Direction) -> None:
        opposite_directions = {
            "UP": "DOWN",
            "DOWN": "UP",
            "LEFT": "RIGHT",
            "RIGHT": "LEFT",
        }
        if opposite_directions.get(self._direction) != new_direction:
            self._direction = new_direction

    def process_key(self, key: int) -> None:
        if key == curses.KEY_UP:
            self.change_direction("UP")
        elif key == curses.KEY_DOWN:
            self.change_direction("DOWN")
        elif key == curses.KEY_LEFT:
            self.change_direction("LEFT")
        elif key == curses.KEY_RIGHT:
            self.change_direction("RIGHT")
        elif key == ord("1"):
            self._difficulty = "EASY"
        elif key == ord("2"):
            self._difficulty = "MEDIUM"
        elif key == ord("3"):
            self._difficulty = "HARD"
