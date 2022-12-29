import time

import cv2
import keyboard
import numpy as np
import pyautogui
from plyer import notification

from coords import Buttons
from objects import Point
from utils import click, ensure_focused_window, sleep

if __name__ == "__main__":

    notification.notify(
        title="BulletForce Money Bot",
        message=f"The bot has finished successfully!",
        timeout=5,
        app_icon="src/python.ico",
    )
