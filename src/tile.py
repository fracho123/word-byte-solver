import os
from PIL import Image
from itertools import product

def tile(filename, dir_in, dir_out):
    name, ext = os.path.splitext(filename)
    img = Image.open(os.path.join(dir_in, filename))
    w, h = img.size
    w_d = int(w / 8)
    h_d = int(h / 9)

    grid = product(range(0, h-h%h_d, h_d), range(0, w-w%w_d, w_d))
    for i, j in grid:
        box = (j, i, j+w_d, i+h_d)
        out = os.path.join(dir_out, f'{name}_{i}_{j}{ext}')
        img.crop(box).save(out)
