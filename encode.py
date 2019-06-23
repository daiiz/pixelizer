# coding=utf-8
import sys, os
import numpy as np
from svg_writer import svg_a, svg_b
from html_writer import html_a
from PIL import Image

def to_matrix(raw_image_path, file_name):
  im = Image.open(raw_image_path)
  (height, width, depth) = np.shape(np.array(im))
  if (width >= 500 or height >= 500) and (not raw_image_path.endswith('.png')):
    im = im.resize((int(width / 5), int(height / 5)), Image.LANCZOS)
  im.save('./tmp/'+ file_name +'.bmp')
  im = Image.open('./tmp/'+ file_name +'.bmp')
  return np.array(im)

if __name__ == '__main__':
  args = sys.argv
  if len(args) <= 1 or len(args[1]) == 0:
    print('Input image is required.')
    exit()
  raw_image_path = args[1]
  
  file_name = raw_image_path.split('/').pop().split('.')[0]
  if not os.path.exists(raw_image_path):
    print('Input image is not found.')
    exit()
  mat = to_matrix(raw_image_path, file_name)
  
  px_str = '@'
  if (len(args) > 2):
    px_str = args[2]

  print(file_name, px_str)
  text = html_a(mat, px_str)

  with open('./html/' + file_name + '.a.svg', mode='w') as f:
    f.write(text)
