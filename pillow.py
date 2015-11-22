#pillow 

from PIL import Image
im=Image.open('test.png')
print im.format,im.size,im.mode
im.thumbnail((40,40))
print im.format,im.size,im.mode
im.save('thumb.jpg','JPEG')

import sys
print sys.path
