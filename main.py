from name_generator import *

from PIL import Image, ImageColor
from secrets import *

colors = [(0,0,0), (255,255,255), (128,0,0), (255,0,0), (0,255,0), (255,255,0), (192, 192, 192), (192, 192, 192), (192, 192, 192), (0,0,255), (0,255,255), (255,0,255), (255,105,180)]

im = Image.new(mode="RGBA", size=(380,380), color=(192, 192, 192))

for z in range(100):
    x_ax = 38
    y_ax = 38


    for i in range(64):
        color = choice(colors)
        if x_ax == 342:
            x_ax = 38
            y_ax += 38
            for x in range(x_ax, x_ax + 38):
                for y in range(y_ax, y_ax + 38):
                    im.putpixel((x, y), color)
        else:
            for x in range(x_ax, x_ax + 38):
                for y in range(y_ax, y_ax + 38):
                    im.putpixel((x, y), color)

        x_ax += 38
    nft = generate_name()
    im.save(nft + '.png')