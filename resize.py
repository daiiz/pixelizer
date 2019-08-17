from PIL import Image
import sys

if __name__ == '__main__':
  args = sys.argv
  if len(args) <= 1 or len(args[1]) == 0:
    print('Input image path is required.')
    exit()
  raw_image_path = args[1]

  im = Image.open(raw_image_path)

  pptrIm = Image.open('./pptr/a.png')
  print(im.width, im.height)
  print(pptrIm.width, pptrIm.height)

  outIm = pptrIm.resize((im.width * 2, im.height * 2), Image.LANCZOS)
  outIm.save('./pptr/a.2x.png')
