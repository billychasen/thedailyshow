import aligner
from iterator import Iterator
import os
import throttle
import sys

source_dir = "/Volumes/chillydisk/dailyshow"
dest_dir = "/Volumes/chillydisk/ds_processed"

# for going from raw screenshots to a directory to get ready for alignment
#iterator = Iterator()
#iterator.iterate_copy(source_dir, dest_dir)

iterator = Iterator()
images = iterator.iterate(dest_dir)
align_to = images[0]
images.pop(0)
last_episode = ""

@throttle.Timeout(seconds=60)
def process_image(image):
    align = aligner.Aligner()
    align.add_face_no_throttle(globals()["align_to"])
    
    episode = image.split("/")[-1].replace(".jpg", "").split("_")[1]
    if episode == globals()["last_episode"]:
        os.remove(image)
        return False

    try:
        align.add_face(image)
    except:
        print "removing " + image
        os.remove(image)
        return False

    align.align(image)
    globals()["last_episode"] = episode
    return True

if len(sys.argv) == 2:
    start = 0
    match = sys.argv[1]
    for image in images:
        start += 1
        if image.endswith(match):
            break
    images = images[start:]

for image in images:
    try:
        if process_image(image):
            print image
    except throttle.TimeoutError:
        print "timeout " + image

