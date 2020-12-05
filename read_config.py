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

def get_config():
    read_config()
    return CONFIG
