from PIL import Image, ImageDraw
import sys

image_file = sys.argv[1]

img = Image.open(image_file)
color_space = Image.new('RGB', (512, 512), (255, 255, 255))

colors = img.getcolors(10000000)
colors.sort()
regular_colors = []
count = 0
count_total = 0
for color in colors:
    x = color[1][0] * 2
    y = color[1][1] * 2
    x1 = 510 - color[1][0] * 2
    y1 = 510 - color[1][2] * 2
    r = color[1][0]
    g = color[1][1]
    b = color[1][2]
    color_space.putpixel((x, y), (r, g, b))
    color_space.putpixel((x+1, y), (r, g, b))
    color_space.putpixel((x, y+1), (r, g, b))
    color_space.putpixel((x+1, y+1), (r, g, b))


print(color_space.size)
draw = ImageDraw.Draw(color_space)
for i in range(0, color_space.size[0], int(color_space.size[0]/4)):
    draw.line((0, i, color_space.size[0], i), fill=255)
    draw.line((i, 0, i, color_space.size[0]), fill=255)
del draw


color_space.save('color-map-' + img.filename)