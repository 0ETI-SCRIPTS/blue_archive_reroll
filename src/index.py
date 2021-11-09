import os
import time

import pyautogui
from PIL.ImageOps import grayscale

from helpers.execution import (
    locate,
    guarantee_img_click,
    spam_click,
)

from helpers.scene import (
    extract_scene_images,
    skip_dialogue,
    tutbattle1,
    tutbattle2,
    menu,
    stage1,
    execute_scene,
)


def calibrate():
    while True:
        print(f"{pyautogui.position()}")
        time.sleep(1)


# tutbattle1()
# skip_dialogue()
# skip_dialogue()
# tutbattle2()
# menu()
# stage1()
# execute_scene("menu2")
execute_scene("recruit2")


# calibrate()
