from PIL import Image
import sys

if __name__ == '__main__':
  args = sys.argv
  if len(args) <= 1 or len(args[1]) == 0:
    print('Input image path is required.')
    exit()
  raw_image_path = args[1]

  im = Image.open(raw_image_path)
  outIm = im.resize((im.width * 10, im.height * 10), Image.LANCZOS)
  # Image.LANCZOS)
  outIm.save('./tmp/x_a.png')
