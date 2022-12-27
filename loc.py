import time

import keyboard
from pyautogui import position

wanted_positions: list[tuple] = []

# [Point(x=1939, y=389), Point(x=1661, y=784), Point(x=2042, y=1241)]

while not keyboard.is_pressed("q"):
    pos = position()

    if keyboard.is_pressed("x"):
        wanted_positions.append(pos)
        time.sleep(0.5)

    print(pos)

from pprint import pprint

pprint(wanted_positions)
