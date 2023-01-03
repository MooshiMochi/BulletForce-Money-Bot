import os
import time
from typing import List, Tuple

import cv2
import keyboard
import numpy as np
import pyautogui
import win32api
import win32con
import win32gui
from pyautogui import position

from coords import Buttons
from objects import Point


def get_screen_size() -> Tuple[int, int]:
    """Returns the size of the screen"""
    return pyautogui.size()


def sleep(seconds: int) -> None:
    start = time.time()
    while not keyboard.is_pressed("q") and time.time() - start < seconds:
        time.sleep(0.1)


def click(point: Point = None):
    """Clicks at the given point. If no point is given, it will click at the current mouse position"""
    if not point:
        point = Point(*position())
    else:
        point.move_to_pos()

    sleep(0.2)

    print(f"Clicking at: {point.x}, {point.y}")
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, point.x, point.y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, point.x, point.y)
    # print(f"Current Position: {position()}")


def ensure_focused_window():
    """If the current focused window is not OperaGX, focus it"""

    win32gui.EnumWindows(
        lambda hwd, _: win32gui.SetForegroundWindow(hwd)
        if win32gui.GetWindowText(hwd).endswith("Opera")
        else None,
        None,
    )
    sleep(1)


def back_to_start(screen_xy: Point, w: int, h: int):
    coord = Buttons.back.get_screen_coords(screen_xy, (w, h))
    for _ in range(2):
        click(coord)
        sleep(2)


def get_region():
    coordinates: List[Tuple, Tuple, Tuple, Tuple] = []

    while not keyboard.is_pressed("q"):
        if len(coordinates) == 4:
            return coordinates

        if keyboard.is_pressed("x"):
            position = pyautogui.position()
            print(f"Recording: {position}")

            coordinates.append((position.x, position.y))
            sleep(0.5)

            print("Ready to read!")

    return coordinates


def show_mouse_pos():
    while not keyboard.is_pressed("q"):
        print(pyautogui.position())
        sleep(0.5)


def is_ad_done() -> bool:
    x = wait_for_image("src/fb_logo.png", timeout=15)
    print(f"Ad Done: {x}")
    return x


def find_image_on_screen(image_path: str) -> tuple[Point, bool]:
    assert os.path.exists(image_path), "Image not found"

    ensure_focused_window()
    sleep(1)

    screen = pyautogui.screenshot()
    screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)

    template = cv2.imread(image_path, 0)

    result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    threshold = 0.7

    if max_val >= threshold:
        print(f"Image {image_path} found at: {max_loc}")
    else:
        print(f"Image {image_path} not found. Max value: {max_val}")

    return Point(*max_loc), max_val >= threshold


def wait_for_image(image_path: str, timeout: int = 10):
    start = time.time()
    while time.time() - start < timeout and not keyboard.is_pressed("q"):
        if find_image_on_screen(image_path)[1]:
            return True
        sleep(1)
    return False


def login(screen_xy: Point, width: int, height: int):

    get_coords_params = [screen_xy, (width, height)]

    # full_screen_coords = Buttons.full_screen.get_screen_coords(*get_coords_params)
    play_now = Buttons.play_now.get_screen_coords(*get_coords_params)
    confirm = Buttons.confirm.get_screen_coords(*get_coords_params)
    settings = Buttons.settings.get_screen_coords(*get_coords_params)
    btn_login = Buttons.login.get_screen_coords(*get_coords_params)
    login_confirm = Buttons.login_confirm.get_screen_coords(*get_coords_params)
    btn_back = Buttons.back.get_screen_coords(*get_coords_params)

    pyautogui.press("F5")
    sleep(2)

    click(play_now)
    sleep(13)

    wait_for_image("src/confirm.png", 15)

    click(confirm)
    sleep(2)

    click(settings)
    sleep(2)

    click(btn_login)
    sleep(2)

    click(login_confirm)
    sleep(2)

    wait_for_image("src/arrow_back.png", 15)

    click(btn_back)
    sleep(2)


def make_money(screen_xy: Point, screen_width: int, screen_height: int):

    login(screen_xy, screen_width, screen_height)
    sleep(1)

    buttons = [Buttons.get_ads, Buttons.watch_ads, Buttons.ad_done]
    wait_times = [1.0, 12.0, 1.0]

    for i in range(len(buttons)):
        buttons[i] = buttons[i].get_screen_coords(
            screen_xy, (screen_width, screen_height)
        )

    attempt = 1

    while not keyboard.is_pressed("q"):

        for index, (button, time_to_wait) in enumerate(zip(buttons, wait_times)):
            if index == 2:

                for c in range(3):
                    if not is_ad_done():
                        if c == 2:

                            if attempt == 1:
                                attempt += 1
                                back_to_start(screen_xy, screen_width, screen_height)
                                break
                            attempt = 1
                            print("Game is broken? Restarting...")
                            login(screen_xy, screen_width, screen_height)
                            sleep(1)
                            break
                    else:
                        attempt = 1
                        break
                    sleep(3)

            click(button)
            sleep(time_to_wait)
