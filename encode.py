# coding=utf-8
import sys, os
import numpy as np
from svg_writer import svg_a, svg_b
from html_writer import html_a
from PIL import Image

def to_matrix(raw_image_path, dpr=1):
  im = Image.open(raw_image_path)
  (height, width, depth) = np.shape(np.array(im))
  # im = im.resize((100,100), Image.LANCZOS)
  if width >= 500 or height >= 500:
    im = im.resize((int(width / 5), int(height / 5)), Image.LANCZOS)
  im.save('./tmp/a.jpg')
  return np.array(im)

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
  mat = to_matrix(raw_image_path, dpr=10)
  
  # text = svg_b(mat)
  text = html_a(mat)
  file_name = raw_image_path.split('/').pop().split('.')[0]

  # with open('./svg/' + file_name + '.b.svg', mode='w') as f:
    # f.write(text)

  with open('./html/' + file_name + '.a.svg', mode='w') as f:
    f.write(text)
