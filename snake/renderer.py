import curses
from typing import List, Tuple

from snake.snake import Snake
from snake.food import Food
from snake.input_handler import Difficulty


class Renderer:
    def __init__(self, stdscr: curses.window) -> None:
        self.stdscr = stdscr
        self.score = 0
        self.difficulty: Difficulty = "MEDIUM"
        self.game_over = False
        self._init_curses()

    def _init_curses(self) -> None:
        curses.curs_set(0)
        self.stdscr.nodelay(True)
        self.stdscr.timeout(100)
        curses.start_color()
        curses.use_default_colors()
        curses.init_pair(1, curses.COLOR_GREEN, -1)
        curses.init_pair(2, curses.COLOR_RED, -1)
        curses.init_pair(3, curses.COLOR_YELLOW, -1)
        curses.init_pair(4, curses.COLOR_WHITE, -1)

    def get_board_dimensions(self) -> Tuple[int, int]:
        height, width = self.stdscr.getmaxyx()
        return width, height

    def draw_border(self, width: int, height: int) -> None:
        try:
            for x in range(width):
                self.stdscr.addch(0, x, '#')
                self.stdscr.addch(height - 1, x, '#')
            for y in range(height):
                self.stdscr.addch(y, 0, '#')
                self.stdscr.addch(y, width - 1, '#')
        except curses.error:
            pass

    def draw_snake(self, snake_body: List[Tuple[int, int]]) -> None:
        try:
            for i, (x, y) in enumerate(snake_body):
                if i == 0:
                    self.stdscr.addch(y, x, '@', curses.color_pair(1))
                else:
                    self.stdscr.addch(y, x, 'O', curses.color_pair(1))
        except curses.error:
            pass

    def draw_food(self, food_position: Tuple[int, int]) -> None:
        try:
            x, y = food_position
            self.stdscr.addch(y, x, '*', curses.color_pair(2))
        except curses.error:
            pass

    def draw_score(self, score: int, width: int) -> None:
        try:
            score_text = f"Score: {score}"
            self.stdscr.addstr(0, width - len(score_text) - 2, score_text, curses.color_pair(3))
        except curses.error:
            pass

    def draw_difficulty(self, difficulty: Difficulty, width: int) -> None:
        try:
            diff_text = f"Difficulty: {difficulty}"
            self.stdscr.addstr(1, width - len(diff_text) - 2, diff_text, curses.color_pair(3))
        except curses.error:
            pass

    def draw_game_over(self, final_score: int, width: int, height: int) -> None:
        try:
            game_over_text = "GAME OVER"
            score_text = f"Final Score: {final_score}"
            restart_text = "Press any key to exit"
            
            center_y = height // 2
            center_x = width // 2
            
            self.stdscr.addstr(center_y - 1, center_x - len(game_over_text) // 2, game_over_text, curses.color_pair(2) | curses.A_BOLD)
            self.stdscr.addstr(center_y, center_x - len(score_text) // 2, score_text, curses.color_pair(3))
            self.stdscr.addstr(center_y + 1, center_x - len(restart_text) // 2, restart_text, curses.color_pair(4))
        except curses.error:
            pass

    def render(
        self,
        snake: Snake,
        food: Food,
        score: int,
        difficulty: Difficulty,
        game_over: bool
    ) -> None:
        self.score = score
        self.difficulty = difficulty
        self.game_over = game_over

        self.stdscr.clear()
        width, height = self.get_board_dimensions()
        
        self.draw_border(width, height)
        
        if not self.game_over:
            self.draw_snake(snake.get_body_positions())
            self.draw_food(food.get_position())
            self.draw_score(score, width)
            self.draw_difficulty(difficulty, width)
        else:
            self.draw_game_over(score, width, height)
        
        self.stdscr.refresh()
