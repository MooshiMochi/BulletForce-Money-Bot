import win32api


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

    def move_to_pos(self):
        """Moves the mouse to the position of the point"""
        win32api.SetCursorPos((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)


class Button:
    def __init__(self, name: str, x_mult: float, y_mult: float):
        self.name = name
        self.x_mult = x_mult
        self.y_mult = y_mult

    def get_coords(self, game_size: tuple[int, int]) -> Point:
        """Gets the coordinates of the button relative to the game screen"""
        return Point(int(self.x_mult * game_size[0]), int(self.y_mult * game_size[1]))

    def get_screen_coords(
        self, game_top_left: Point, game_size: tuple[int, int]
    ) -> Point:
        """Gets the coordinates of the button relative to the computer screen"""
        location = self.get_coords(game_size)
        return game_top_left + location

    def __repr__(self):
        return f"Button({self.name}, {self.x_mult}, {self.y_mult})"

    def __str__(self):
        return f"{self.name}: {self.x_mult}, {self.y_mult}"
