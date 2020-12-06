import os
from os.path import expanduser
import json

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
HOME = expanduser("~")

def read_config():
    with open(COLLECT_CONFIG_PATH, 'r') as file:
        json_str = file.read().replace('\n', '')
        loaded_config = json.loads(json_str)
        CONFIG["assetsPath"] =  HOME + loaded_config["assetsPath"]
        CONFIG["desktopPath"] = loaded_config["desktopPath"]
        CONFIG["mobilePath"] = loaded_config["mobilePath"]
        CONFIG["minWidth"] = loaded_config["minWidth"]
        CONFIG["minHeight"] = loaded_config["minHeight"]
        CONFIG["discardSquares"] = loaded_config["discardSquares"]
        CONFIG["autoRemoveDuplicates"] = loaded_config["autoRemoveDuplicates"]
        CONFIG["saveDiscarded"] = loaded_config["saveDiscarded"]
        CONFIG["discardPath"] = loaded_config["discardPath"]
        CONFIG["scriptDir"] = SCRIPT_DIR

def setup_dirs():
    desktop_path = CONFIG["desktopPath"]
    mobile_path = CONFIG["mobilePath"]
    discard_path = CONFIG["discardPath"]
    if not os.path.exists(desktop_path):
        os.mkdir(desktop_path)
    if not os.path.exists(mobile_path):
        os.mkdir(mobile_path)
    if CONFIG["saveDiscarded"] and not os.path.exists(discard_path):
        os.mkdir(discard_path)

def get_config():
    read_config()
    setup_dirs()
    return CONFIG
