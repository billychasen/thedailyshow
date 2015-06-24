# About this

This is	a quick	and dirty set of python	scripts	to download images of The Daily	Show, align each frame to the previous one (based on Jon's face and using Microsoft's Project Oxford) and then create a movie out of it. You can view the final product on [youtube](https://www.youtube.com/watch?v=EC0Xfv433n8&feature=youtu.be) and here's a [quick gif](http://gfycat.com/FirstRealBoa).

# Main files

* crawl.py - This is the script that goes through each season, tries different URL formats for the thumbnail and downloads it.
* process.py - Align each image to the first image. By aligning every image to the very first image, Jon stays in the same exact place.
* faces.py - Talks with Project Oxford and gets the rectangle for a face in a photo.
* converter.py - Copies all the images to one directory and renames them all in format image_n.jpg for ffmpeg
