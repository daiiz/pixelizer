# coding=utf-8
from PIL import Image
import sys

def main(raw_image_path):
  im = Image.open(raw_image_path)
  w = im.width
  h = im.height
  print(w, h)
  rgb_im = im.convert('RGB')
  res = []

  for y in range(0, h):
    row = []
    for x in range(0, w):
      # 0 to 255
      r, g, b = rgb_im.getpixel((x, y))
      row.append([r, g, b])
    res.append(row)
  return res

if __name__ == '__main__':
  args = sys.argv
  if len(args) <= 1 or len(args[1]) == 0:
    print('Input image path is required.')
    exit()
  raw_image_path = args[1]
  raw_image_name = raw_image_path.split('/').pop()
  raw_image_name = raw_image_name \
    .replace('.png', '.txt').replace('.jpg', '.txt')

  color_arr = main(raw_image_path)
  color_map_path = './tmp/v2-2_' + raw_image_name
  print(color_map_path)
  with open(color_map_path, 'w') as f:
    f.write('width={} height={} RGB\n'.format(len(color_arr[0]), len(color_arr)))
    f.write(str(color_arr))
    f.close()
