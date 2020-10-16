import sys
from colorama import Fore,Style
from PIL import Image
def asciifier(name):
    img = Image.open(r'D:\organinzing code is good\project ASCII ART\tahou\tahouimgs\{}'.format(name))
    width, height = img.size
    aspect_ratio = height/width
    new_width = 120
    new_height = aspect_ratio * new_width * 0.55
    img = img.resize((new_width, int(new_height)))
    img = img.convert('L')
    pixels = img.getdata()
    chars = ["B","S","#","&","@","$","%","*","!",":","."]
    new_pixels = [chars[pixel//25] for pixel in pixels]
    new_pixels = ''.join(new_pixels)
    new_pixels_count = len(new_pixels)
    ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
    ascii_image = "\n".join(ascii_image)
    return ascii_image




for i in range(0,7777):
    text=asciifier('frame{}.jpg'.format(i))
    file=open('ascii{}.txt'.format(i),'w')
    file.write(text)
    file.close()


