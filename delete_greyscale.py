'''
Some of the coco images are not rgb so we must get rid of them
'''
import os

from PIL import Image

IMG_PATH = 'images/train2017'
for file in os.listdir(IMG_PATH):
    img = Image.open(os.path.join(IMG_PATH, file))
    if img.mode != 'RGB':
        print('Removing image {} with mode {}'.format(file, img.mode))
        os.remove(os.path.join(IMG_PATH, file))