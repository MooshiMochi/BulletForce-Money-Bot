# While 'q' is not pressed, the program will continue to run

# [Point(x=1939, y=389), Point(x=1661, y=784), Point(x=2042, y=1241)]
import os
import time
from typing import List

import keyboard
import pyautogui
import win32api
import win32con
import win32gui
from pyautogui import position


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

    def move_to_pos(self):
        win32api.SetCursorPos((self.x, self.y))


points: List[Point] = [Point(1939, 389), Point(1661, 784), Point(2042, 1241)]
sleep_time = List = [2.0, 10.0, 2.0]
step = 0


def click(point: Point = None):

    point.move_to_pos()
    time.sleep(0.2)

    print(f"Clicking at: {point.x}, {point.y}")
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, point.x, point.y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, point.x, point.y)
    print(f"Current Position: {position()}")


def ensure_focused_window():
    """If the current focused window is not OperaGX, focus it"""

    win32gui.EnumWindows(
        lambda hwd, param: win32gui.SetForegroundWindow(hwd)
        if win32gui.GetWindowText(hwd).endswith("Opera")
        else None,
        None,
    )
    time.sleep(1)


def back_to_start():
    # p = Point(1670, 390)
    p = Point(439, 488)
    for _ in range(2):
        click(p)
        time.sleep(2)


def is_ad_done():
    """This function will check if the Facebook logo is present. If it is that means the ad is done and we can continue."""

    img_path = "src/fb_logo.png"
    assert os.path.exists(img_path), "Image not found"

    box = pyautogui.locateOnScreen(img_path, grayscale=False, confidence=0.6)

    start_time = time.time()

    while not box:
        if time.time() - start_time > 10:
            back_to_start()
            return True

        time.sleep(2)
        box = pyautogui.locateOnScreen(img_path, grayscale=False, confidence=0.6)
    return True


def main():
    ensure_focused_window()

    while not keyboard.is_pressed("q"):
        for index, (point, tts) in enumerate(zip(points, sleep_time)):
            if index == 2:
                is_ad_done()
            click(point)
            time.sleep(tts)


if __name__ == "__main__":
    time.sleep(3)

    main()
