from PIL import Image

if __name__ == '__main__':
  im = Image.open('./raw/pancake.jpg')

  pptrIm = Image.open('./pptr/a.png')
  print(im.width, im.height)
  print(pptrIm.width, pptrIm.height)

  outIm = pptrIm.resize((im.width * 4, im.height * 4), Image.LANCZOS)
  outIm.save('./pptr/a.2x.png')
