from enum import Enum
from typing import List, Tuple


class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)


class Snake:
    def __init__(self, start_position: Tuple[int, int] = (10, 10)):
        self._body: List[Tuple[int, int]] = [
            start_position,
            (start_position[0], start_position[1] + 1),
            (start_position[0], start_position[1] + 2),
        ]
        self._direction: Direction = Direction.UP
        self._growing: bool = False

    def move(self) -> None:
        head_x, head_y = self._body[0]
        dx, dy = self._direction.value
        new_head = (head_x + dx, head_y + dy)
        self._body.insert(0, new_head)
        if not self._growing:
            self._body.pop()
        self._growing = False

    def grow(self) -> None:
        self._growing = True

    def get_head_position(self) -> Tuple[int, int]:
        return self._body[0]

    def get_body_positions(self) -> List[Tuple[int, int]]:
        return list(self._body)

    def check_self_collision(self) -> bool:
        return self._body[0] in self._body[1:]

    def set_direction(self, direction: Direction) -> None:
        opposite_direction = {
            Direction.UP: Direction.DOWN,
            Direction.DOWN: Direction.UP,
            Direction.LEFT: Direction.RIGHT,
            Direction.RIGHT: Direction.LEFT,
        }
        if direction != opposite_direction.get(self._direction):
            self._direction = direction
