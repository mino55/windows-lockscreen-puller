import os

TARGET_PATH = os.getcwd()
DISCARD_PATH = os.getcwd() + "/discarded/"

discarded_files = []

def are_dublicates(img_a_path, img_b_path):
  return open(img_a_path, "rb").read() == open(img_b_path, "rb").read()

def is_image(path):
    if path.endswith('.png') or path.endswith('.jpg'):
        return True
    return False

def different_names(target_file, other_file):
    return os.path.basename(target_file) != os.path.basename(other_file)

def discard(img):
    discarded_files.append(img)
    os.rename(img, DISCARD_PATH + "/" + os.path.basename(img))

def is_candidate(target_file, other_file):
    return different_names(target_file, other_file) and is_image(other_file)

def is_discarded(file):
    return file in discarded_files

print "Looking for duplicates in: " + TARGET_PATH
print "Discarding duplicates to: " + DISCARD_PATH
raw_input('Is this ok? If so, press any key to continue')
print ""

for root, dirs, files in os.walk(TARGET_PATH):
    for target_file in files:
        if is_discarded(target_file) or not is_image(target_file):
            continue
        print "Searching for duplicates of " + target_file
        dups = 0
        for other_file in files:
            if is_discarded(other_file): continue
            if is_candidate(target_file, other_file):
                if are_dublicates(target_file, other_file):
                    discard(other_file)
                    dups += 1
                    print "- Found duplicate " + other_file
        if (dups == 0): print "- No duplicates found"
        print ""

raw_input('All files searched. Press any key to continue')
