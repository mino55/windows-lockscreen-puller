import os
import time
import uuid
from PIL import Image
from datetime import date
import shutil
import importlib
import collect_config
from os.path import expanduser

HOME = expanduser("~")
ASSET_PATH = HOME + collect_config.collect_from

def start_at(asset_path):
    for root, dirs, files in os.walk(asset_path):
        sift_files(files, root)
        for dir in dirs:
            sift_files(os.listdir(dir), dir)

def sift_files(files, in_dir):
    for file in files:
        path_to_image = os.path.join(in_dir, file)
        image = open_image(path_to_image)
        if image != None: sift_image(image, path_to_image, os.getcwd())
        else: print(str(file) + ' is not an image file.')

def open_image(path_to_image):
    try:
        return Image.open(path_to_image)
    except:
        return None

def sift_image(image, copy_from_path, copy_to_dir):
    width, height = image.size
    if width > 500 and height > 500:
        name = str(date.today()) + '-' + str(uuid.uuid4()) + '.jpg'
        copy_to_path = os.path.join(copy_to_dir, name)
        shutil.copy(copy_from_path, copy_to_path)
        print('From: ' + copy_from_path)
        print('Created: ' + name + ' (' + str(width) + 'x' + str(height) + ')')

def get_config_path():
    try:
        print('Collect from:' + ASSET_PATH)
        input('Is this ok? If so, press any key to continue')
        return ASSET_PATH
    except:
        print('WARNING: Collect_from inside of collect_config.py not found')
        print('Collect from: ' + os.getcwd())
        input('Is this ok? If so, press any key to continue')
        return os.getcwd()


start_at(get_config_path())
input('Done! Press any key to quit')
