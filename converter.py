from iterator import Iterator
import os
import sys

source_dir = "/Volumes/chillydisk/ds_video2"

"""
   This just takes all the images in the source directory and numbers them
   so that you can run ffmpeg on them.
"""

iterator = Iterator()
images = iterator.iterate(source_dir)

x = 0
for image in images:
    new_name = "/".join(image.split("/")[:-1]) + ("/image_%04d.jpg" % x)
    x += 1
    os.rename(image, new_name)

# ffmpeg -f image2 -framerate 30 -pattern_type sequence -start_number 0 -r 15 -i image_%04d.jpg -s 1080x608 -vcodec libx264 -b 5000k video.avi
