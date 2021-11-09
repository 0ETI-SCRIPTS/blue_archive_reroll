import os
import time

import pyautogui
from .execution import (
    guarantee_img_click, spam_click_until_image_found, spam_click_until_image_gone, wait_until_image_found)

IMAGE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "scenes")


def extract_scene_images(scene: str):
    DIR = os.path.join(IMAGE_DIR, scene)

    items = list(filter(
        lambda file: file.endswith(".png"),
        os.listdir(DIR)
    ))
    items.sort(
        key=lambda item: int(item.split(".")[0].split("-")[0])
    )

    return list(map(
        lambda file: os.path.join(DIR, file),
        items
    ))


def execute_scene(scene: str):
    for img_path in extract_scene_images(scene):

        wait = img_path.split("/")[-1].split(".")[0].split("-")[-1] == "w"

        if wait:
            wait_until_image_found(img_path)
        else:
            spam_click_until_image_found(img_path)

        guarantee_img_click(img_path)

        time.sleep(0.5)
