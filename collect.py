import os
import time
import uuid
from PIL import Image
from datetime import date
import shutil
import importlib

from read_config import get_config
from remove_duplicate_images import remove_duplicates

CONFIG = get_config()

class ImageFormat:
    DESKTOP = "desktop"
    MOBILE = "mobile"

def start_at(asset_path):
    for root, dirs, files in os.walk(asset_path):
        sift_files(files, root)
        for dir in dirs:
            sift_files(os.listdir(dir), dir)

def sift_files(files, in_dir):
    for file in files:
        path_to_file = os.path.join(in_dir, file)
        image = open_image(path_to_file)
        if image == None:
            print(str(file) + ' is not an image file.')
            return
        print("For file: " + str(file));
        sift_image(image, path_to_file)

def open_image(path_to_image):
    try:
        return Image.open(path_to_image)
    except:
        return None

def sift_image(image, copy_from_path):
    if not image_is_valid(image):
        print("Fails validation")
        print('--- --- --- --- ---')
        return
    img_format = image_format(image)
    if img_format == ImageFormat.DESKTOP:
        save_image(image, copy_from_path, CONFIG["desktopPath"])
    if img_format == ImageFormat.MOBILE:
        save_image(image, copy_from_path, CONFIG["mobilePath"])


def image_is_valid(image):
    width, height = image.size
    if CONFIG["discardSquares"] and width == height:
        print("Square image: " + str(width) + ", " + str(height))
        return False
    if CONFIG["minWidth"] and width < CONFIG["minWidth"]:
        print("Too small width: " + str(width))
        return False
    if CONFIG["minHeight"] and height < CONFIG["minHeight"]:
        print("Too small height: " + str(height))
        return False
    return True

def image_format(image):
    width, height = image.size
    if width > height:
        return ImageFormat.DESKTOP
    if height > width:
        return ImageFormat.MOBILE
    else:
        exc_msg = "Image with errous width, height: " + str(width) + ", " + str(height)
        raise Exception(exc_msg)


def save_image(image, copy_from_path, copy_to_dir):
    width, height = image.size
    name = str(date.today()) + '-' + str(uuid.uuid4()) + '.jpg'
    copy_to_path = os.path.join(copy_to_dir, name)
    shutil.copy(copy_from_path, copy_to_path)
    print('Created: ' + name + ' (' + str(width) + 'x' + str(height) + ')')
    print('From: ' + copy_from_path)
    print('To: ' + copy_to_path)
    print('--- --- --- --- ---')

def get_config_path():
    try:
        print('Collect from: ' + CONFIG["assetsPath"])
        print('Collect to: ' +  CONFIG["scriptDir"])
        input('Is this ok? If so, press any key to continue')
        print('--- --- --- --- ---')
        return CONFIG["assetsPath"]
    except:
        print('WARNING: Collect_from inside of collect_config.py not found')

start_at(get_config_path())
remove_duplicates()
input('Done! Press any key to quit')
