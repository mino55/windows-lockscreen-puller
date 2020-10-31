# TODO: Rewrite this script to iterate through every directory in cd
# and copy every found file into cd
import os
import time
import uuid
from PIL import Image
from datetime import date
import shutil

def open_image(path_to_image):
    try:
        return Image.open(path_to_image)
    except:
        return None

def sift_image(image, copy_from_file, copy_to_dir):
    width, height = image.size
    if width > 500 and height > 500:
        name = str(date.today()) + '-' + str(uuid.uuid4()) + '.jpg'
        copy_to_file = os.path.join(copy_to_dir, name)
        shutil.copy(copy_from_file, copy_to_file)
        print 'Created: ' + name + ' (' + str(width) + 'x' + str(height) + ')'

def start_at(asset_path):
    for dir, subdir, files in os.walk(asset_path):
        for file in files:
            path_to_image = os.path.join(dir, file)
            image = open_image(path_to_image)
            if image != None: sift_image(image, path_to_image, os.getcwd())
            else: print(str(file) + ' is not an image file.')

local_path = os.getcwd()
start_at(local_path)
