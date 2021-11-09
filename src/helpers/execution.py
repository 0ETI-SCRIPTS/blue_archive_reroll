import os
import time
from PIL.ImageOps import grayscale
import pyautogui

last_location = pyautogui.Point(1300, 500)


def locate(image_path: str):
    location = pyautogui.locateCenterOnScreen(
        image_path,
        # grayscale=True,
        confidence=0.90
    )

    return pyautogui.Point(int(location.x / 2), int(location.y / 2)) if location else None


def click_point(location: pyautogui.Point):
    pyautogui.click(location)
    last_location = location


def guarantee_img_click(image_path: str):

    # Keep searching until location hit
    location = None
    while not location:
        location = locate(image_path)

    # Keep clicking until location dissapears
    while location:
        click_point(location)
        location = locate(image_path)
        # Sleep to deal w. sparkle effect
        time.sleep(1)


def spam_click():
    for i in range(3):
        click_point(last_location)
        time.sleep(0.3)


def spam_click_until_image_found(img_path: str):
    while not locate(img_path):
        spam_click()


def spam_click_until_image_gone(img_path: str):
    while locate(img_path):
        spam_click()


def wait_until_image_found(image_path: str):
    while not locate(image_path):
        time.sleep(0.5)
