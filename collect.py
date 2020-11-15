import os
import time
import uuid
from PIL import Image
from datetime import date
import shutil
import importlib
from os.path import expanduser
import pathlib
from pathlib import PurePosixPath
import json

HOME = expanduser("~")
SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
COLLECT_CONFIG_PATH = os.path.join(SCRIPT_DIR, 'config.json')
CONFIG = {
  "assetsPath": None,
  "desktopPath": None,
  "mobilePath": None,
  "minWidth": None,
  "minHeight": None,
  "autoRemoveDuplicates": None,
  "saveDiscarded": None,
  "discardPath": None
}

def read_config():
  with open(COLLECT_CONFIG_PATH, 'r') as file:
    json_str = file.read().replace('\n', '')
    loaded_config = json.loads(json_str)
    CONFIG["assetsPath"] = HOME + loaded_config["assetsPath"]
    CONFIG["desktopPath"] = loaded_config["desktopPath"]
    CONFIG["mobilePath"] = loaded_config["mobilePath"]
    CONFIG["minWidth"] = loaded_config["minWidth"]
    CONFIG["minHeight"] = loaded_config["minHeight"]
    CONFIG["autoRemoveDuplicates"] = loaded_config["autoRemoveDuplicates"]
    CONFIG["saveDiscarded"] = loaded_config["saveDiscarded"]
    CONFIG["discardPath"] = loaded_config["discardPath"]

def start_at(asset_path):
    for root, dirs, files in os.walk(asset_path):
        sift_files(files, root)
        for dir in dirs:
            sift_files(os.listdir(dir), dir)

def sift_files(files, in_dir):
    for file in files:
        path_to_image = os.path.join(in_dir, file)
        image = open_image(path_to_image)
        if image != None: sift_image(image, path_to_image, SCRIPT_DIR)
        else: print(str(file) + ' is not an image file.')

def open_image(path_to_image):
    try:
        return Image.open(path_to_image)
    except:
        return None

def sift_image(image, copy_from_path, copy_to_dir):
    width, height = image.size
    if width > CONFIG["minWidth"] and height > CONFIG["minHeight"]:
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
        print('Collect to: ' +  SCRIPT_DIR)
        input('Is this ok? If so, press any key to continue')
        print('--- --- --- --- ---')
        return CONFIG["assetsPath"]
    except:
        print('WARNING: Collect_from inside of collect_config.py not found')


read_config()
start_at(get_config_path())
input('Done! Press any key to quit')
