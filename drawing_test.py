from PIL import Image, ImageDraw
import json

def draw_dots(image_file, json):
    im = Image.open(image_file)
    draw = ImageDraw.Draw(im)

    for coords in json["faceLandmarks"].iteritems():
        x = coords[1]["x"]
        y = coords[1]["y"]
        draw.rectangle((x, y, x+2, y+2), fill='red')
    del draw
    im.save("out.png", "PNG")

with open("test.json", "r") as f:
    js = json.loads(f.read())
    draw_dots("tom.jpg", js)
