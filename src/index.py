import time

import pyautogui

from helpers.scene import execute_scene


def calibrate():
    while True:
        print(f"{pyautogui.position()}")
        time.sleep(1)


# execute_scene("02-dialog1")
# execute_scene("03-battle1")

# execute_scene("04-dialog2")
execute_scene("05-battle2")
execute_scene("06-dialog3")
execute_scene("07-menu1+recruit1")

execute_scene("08-battle3")
execute_scene("09-battle4")
execute_scene("10-menu2")
execute_scene("11-recruit2")
