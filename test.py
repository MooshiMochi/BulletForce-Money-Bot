import os
import time
from typing import List, Tuple

import keyboard
import pyautogui

from main import Point, click, ensure_focused_window


def get_region():
    coordinates: List[Tuple, Tuple, Tuple, Tuple] = []

    while not keyboard.is_pressed("q"):
        if len(coordinates) == 4:
            return coordinates

        if keyboard.is_pressed("x"):
            position = pyautogui.position()
            print(f"Recording: {position}")

            coordinates.append((position.x, position.y))
            time.sleep(0.5)

            print("Ready to read!")

    return coordinates


# box = get_region()
# print(box)


def is_ad_done():
    """This function will check if the Facebook logo is present. If it is that means the ad is done and we can continue."""

    img_path = "src/fb_logo.png"
    assert os.path.exists(img_path), "Image not found"

    box = pyautogui.locateOnScreen(img_path, grayscale=False, confidence=0.6)
    print(box)

    if box:
        return True
    return False


if __name__ == "__main__":

    ensure_focused_window()

    x = is_ad_done()

    print(x)

    # box = get_region()
    # print(box)
