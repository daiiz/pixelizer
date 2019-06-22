# coding=utf-8
import sys, os
import numpy as np
from PIL import Image

def to_matrix(raw_image_path):
  im = Image.open(raw_image_path)
  arr = np.array(im)
  print('shape of raw image:', np.shape(arr))
  return arr

if __name__ == '__main__':
  print(sys.version_info)
  args = sys.argv
  if len(args) <= 1 or len(args[1]) == 0:
    print('Input image is required.')
    exit()
  raw_image_path = args[1]
  if not os.path.exists(raw_image_path):
    print('Input image is not found.')
    exit()
  mat = to_matrix(raw_image_path)
