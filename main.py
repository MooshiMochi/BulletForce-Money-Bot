import keyboard
from plyer import notification
from pyautogui import position

from objects import Point
from utils import ensure_focused_window, make_money, sleep


def init_config() -> Point | None:
    hotkey = "enter"
    notification.notify(
        title="BulletForce Money Bot",
        message=f"Please place your mouse over the full screen button and press '{hotkey}'!",
        timeout=10,
    )

    full_screen_coord = Point(0, 0)
    while not keyboard.is_pressed(hotkey):
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
