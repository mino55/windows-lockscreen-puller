import os

from read_config import get_config

CONFIG = get_config()

def are_dublicates(at_path, img_a_name, img_b_name):
    img_a_path = os.path.join(at_path, img_a_name)
    img_b_path = os.path.join(at_path, img_b_name)

    if not os.path.exists(img_a_path) or not os.path.exists(img_b_path):
        return

    return open(img_a_path, "rb").read() == open(img_b_path, "rb").read()

def is_image(path):
    if path.endswith('.png') or path.endswith('.jpg'):
        return True
    return False

def different_names(target_file, other_file):
    return os.path.basename(target_file) != os.path.basename(other_file)

def discard(img):
    if CONFIG["saveDiscarded"]:
        os.rename(img, os.path.join(CONFIG["discardPath"], os.path.basename(img)))
    else:
        os.remove(img)

def is_candidate(target_file, other_file):
    return different_names(target_file, other_file) and is_image(other_file)

def prompt(target_path):
    print("Looking for duplicates in: " + target_path)
    if CONFIG["saveDiscarded"]:
        print("Discarding duplicates to: " + CONFIG["discardPath"])
    else:
        print("Permanently remove duplicates")
    input("Is this ok? If so, press any key to continue")
    print("")

def get_duplicate_images(at_path, original_image, other_files):
    duplicates = []
    for other_file in other_files:
        if is_candidate(original_image, other_file):
            if are_dublicates(at_path, original_image, other_file):
                duplicates.append(other_file)
    return duplicates

def remove_duplicates_at_path(path):
    discarded_files = []
    for _root, _dirs, files in os.walk(path):
        for target_file in files:
            if not is_image(target_file) or target_file in discarded_files:
                continue

            print("Searching for duplicates of " + target_file)
            duplicate_images = get_duplicate_images(path, target_file, files)

            if len(duplicate_images) == 0: print("- No duplicates found")

            for image in duplicate_images:
                discarded_files.append(image)
                discard(os.path.join(path, image))
                print("- Removed duplicate " + image)
            print("")

def remove_duplicates():
    for path in [CONFIG['desktopPath'], CONFIG['mobilePath']]:
        prompt(path)
        remove_duplicates_at_path(path)
