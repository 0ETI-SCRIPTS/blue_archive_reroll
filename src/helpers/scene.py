import os
import time
from .execution import (
    guarantee_img_click, spam_click_until_image_found, spam_click_until_image_gone, wait_until_image_found)

IMAGE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "img")


def extract_scene_images(scene: str):
    DIR = os.path.join(IMAGE_DIR, scene)

    items = list(filter(
        lambda file: file.endswith(".png"),
        os.listdir(DIR)
    ))
    items.sort(
        key=lambda item: int(item.split(".")[0])
    )

    return list(map(
        lambda file: os.path.join(DIR, file),
        items
    ))


def skip_dialogue():
    guarantee_img_click(os.path.join(IMAGE_DIR, "dialog", "menu.png"))
    guarantee_img_click(os.path.join(IMAGE_DIR, "dialog", "skip.png"))
    guarantee_img_click(os.path.join(IMAGE_DIR, "dialog", "skipconfirm.png"))


def tutbattle1():
    # spam_click_until_image_found(
    #     os.path.join(IMAGE_DIR, "tutbattle1", "1.png"))
    # spam_click_until_image_gone(os.path.join(
    #     IMAGE_DIR, "tutbattle1", "tutlady.png"))
    # guarantee_img_click(os.path.join(IMAGE_DIR, "tutbattle1", "1.png"))
    # guarantee_img_click(os.path.join(IMAGE_DIR, "tutbattle1", "2.png"))
    # spam_click_until_image_found(
    #     os.path.join(IMAGE_DIR, "tutbattle1", "3.png"))
    # spam_click_until_image_gone(os.path.join(
    #     IMAGE_DIR, "tutbattle1", "tutlady.png"))
    # guarantee_img_click(os.path.join(IMAGE_DIR, "tutbattle1", "3.png"))
    # TODO ACTIVATE YUUKA SKILL
    guarantee_img_click(os.path.join(
        IMAGE_DIR, "tutbattle1", "confirmvictory.png"))


def tutbattle2():
    # spam_click_until_image_found(
    #     os.path.join(IMAGE_DIR, "tutbattle1", "tutlady.png"))
    # spam_click_until_image_gone(os.path.join(
    #     IMAGE_DIR, "tutbattle1", "tutlady.png"))
    # spam_click_until_image_found(
    #     os.path.join(IMAGE_DIR, "dialog", "menu.png"))
    # skip_dialogue()
    # spam_click_until_image_found(
    #     os.path.join(IMAGE_DIR, "dialog", "menu.png"))
    # skip_dialogue()
    # spam_click_until_image_found(
    #     os.path.join(IMAGE_DIR, "dialog", "menu.png"))
    # skip_dialogue()
    # spam_click_until_image_found(
    #     os.path.join(IMAGE_DIR, "dialog", "menu.png"))
    # skip_dialogue()
    # spam_click_until_image_found(
    #     os.path.join(IMAGE_DIR, "tutbattle1", "tutlady.png"))
    # spam_click_until_image_gone(os.path.join(
    #     IMAGE_DIR, "tutbattle1", "tutlady.png"))
    # guarantee_img_click(os.path.join(IMAGE_DIR, "tutbattle2", "1.png"))
    # guarantee_img_click(os.path.join(IMAGE_DIR, "tutbattle2", "2.png"))
    # guarantee_img_click(os.path.join(
    #     IMAGE_DIR, "tutbattle1", "confirmvictory.png"))
    # skip_dialogue()
    # time.sleep(5)
    # skip_dialogue()
    spam_click_until_image_found(os.path.join(
        IMAGE_DIR, "tutbattle2", "skipmovie.png"))
    guarantee_img_click(os.path.join(IMAGE_DIR, "tutbattle2", "skipmovie.png"))


def menu():
    # spam_click_until_image_found(os.path.join(
    #     IMAGE_DIR, "menu", "recruit.png"))
    # guarantee_img_click(os.path.join(IMAGE_DIR, "menu", "recruit.png"))
    # guarantee_img_click(os.path.join(IMAGE_DIR, "menu", "free10.png"))
    # guarantee_img_click(os.path.join(IMAGE_DIR, "menu", "confirmpull.png"))
    # guarantee_img_click(os.path.join(IMAGE_DIR, "menu", "skippull1.png"))
    # guarantee_img_click(os.path.join(IMAGE_DIR, "menu", "skippull2.png"))

    spam_click_until_image_found(os.path.join(
        IMAGE_DIR, "menu", "confirmresults.png"))
    guarantee_img_click(os.path.join(IMAGE_DIR, "menu", "confirmresults.png"))


# Will have to test to see if this is really effective
def stage1():
    for img_path in extract_scene_images("stage1"):
        spam_click_until_image_found(img_path)
        guarantee_img_click(img_path)


def menu2():
    for img_path in extract_scene_images("stage1"):
        spam_click_until_image_found(img_path)
        guarantee_img_click(img_path)


def execute_scene(scene: str):
    for img_path in extract_scene_images(scene):

        wait = img_path.split("/")[-1].split(".")[0].split("-")[-1]
        print(wait)

        # wait_until_image_found(img_path)
        # spam_click_until_image_found(img_path)
        # guarantee_img_click(img_path)
        # time.sleep(0.5)
