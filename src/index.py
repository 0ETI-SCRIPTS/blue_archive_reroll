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
# execute_scene("recruit2")

# execute_scene("02-dialog1")
# execute_scene("03-battle1")

# execute_scene("04-dialog2")
# execute_scene("05-battle2")
# execute_scene("06-dialog3")
# execute_scene("07-menu1+recruit1")

execute_scene("08-battle3")
execute_scene("09-battle4")
execute_scene("10-menu2")
execute_scene("11-recruit2")
