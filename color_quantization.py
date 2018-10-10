from PIL import Image
import sys

filename = sys.argv[1]

img = Image.open(filename)
img2 = img.quantize(16, 0)
img2.convert('RGB').save('quantized-med-' + img.filename)

img2 = img.quantize(16, 1)
img2.convert('RGB').save('quantized-max-' + img.filename)

img2 = img.quantize(16, 2)
img2.convert('RGB').save('quantized-oct-' + img.filename)
