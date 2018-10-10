from PIL import Image
import sys
filename = sys.argv[1]
#output_file = sys.argv[2]
pixelation_denominator = int(sys.argv[2])
if pixelation_denominator == 0:
    pixelation_denominator = 100

img = Image.open(filename)
img = img.resize((500, 400))
imgWidth, imgHeight = img.size
pixelation_height_ratio = int(imgHeight/pixelation_denominator)
pixelation_width_ratio = int(imgWidth/pixelation_denominator)

def average_color( x, y, nw, nh, image):
    r, g, b = 0, 0, 0
    count = nw * nh
    for s in range(x, x+nw):
        for t in range(y, y+nh):

            pixelR, pixelG, pixelB = image.getpixel((s, t))
            r += pixelR
            g += pixelG
            b += pixelB
    return (int(r/count), int(g/count), int(b/count))

for x in range(0, imgWidth-1, pixelation_width_ratio):
    for y in range(0, imgHeight-1, pixelation_height_ratio):
        new_rgb = average_color(x,y, pixelation_width_ratio, pixelation_height_ratio, img)
        for a in range(0, pixelation_width_ratio):
            for b in range(0, pixelation_height_ratio):
                img.putpixel((x+a,y+b), new_rgb)

img.save('pixel-' + filename)

