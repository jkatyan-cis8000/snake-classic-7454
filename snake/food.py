import random


class Food:
    def __init__(self, height: int, width: int) -> None:
        self._height = height
        self._width = width
        self._position = (0, 0)
        self._spawn()

    def _spawn(self) -> None:
        y = random.randint(1, self._height - 2)
        x = random.randint(1, self._width - 2)
        self._position = (y, x)

    def spawn(self, height: int, width: int, snake_positions: list[tuple[int, int]]) -> None:
        """Spawn food at a random location not occupied by the snake."""
        self._height = height
        self._width = width
        while True:
            y = random.randint(1, height - 2)
            x = random.randint(1, width - 2)
            if (y, x) not in snake_positions:
                self._position = (y, x)
                break

    def get_position(self) -> tuple[int, int]:
        return self._position

    def respawn(self) -> None:
        self._spawn()
