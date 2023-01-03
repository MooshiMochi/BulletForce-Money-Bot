import keyboard
import win32api
import win32con
from plyer import notification
from pyautogui import position

from objects import Point
from utils import ensure_focused_window, make_money, sleep


def init() -> Point | None:

    notification.notify(
        title="BulletForce Money Bot",
        message=f"Please click the top left and the bottom right corner of the game screen!",
        timeout=10,
    )

    tl, br = Point(0, 0), Point(0, 0)

    full_screen_coord, w, h = Point(0, 0), None, None

    # check if the user clicked the mouse

    while not keyboard.is_pressed():
        if keyboard.is_pressed("q"):
            return
        full_screen_coord = Point(*position())
        sleep(0.1)

    return full_screen_coord


def main():
    ensure_focused_window()

    game_xy, w, h = Point(351, 338), 1844, 1064

    make_money(game_xy, w, h)


if __name__ == "__main__":
    sleep(2)

    exc: Exception = None
    try:
        main()

    except Exception as exc:
        notification.notify(
            title="BulletForce Money Bot",
            message=f"The bot has crashed! More details in console.",
            timeout=10,
            app_icon="src/python.ico",
        )

    if not exc:
        notification.notify(
            title="BulletForce Money Bot",
            message=f"The bot has been stopped.",
            timeout=5,
            app_icon="src/python.ico",
        )
