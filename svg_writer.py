import numpy as np

svg_tail = '</svg>'

def svg_head(mat, pixel_width):
  (height, width, depth) = np.shape(mat)
  return ''.join([
    '<svg xmlns="http://www.w3.org/2000/svg" '
    'width="' + str(width * pixel_width) + '" ',
    'height="' + str(height * pixel_width) + '" ',
    'viewBox="0 0 ' + str(width * pixel_width) + ' ' + str(height * pixel_width) + '">'
  ])

def rect_1x1px(x, y, r, g, b):
  return ''.join([
    '<rect width="'+ str(1) +'" height="'+ str(1) +'" ',
    'x="'+ str(x) +'" ',
    'y="'+ str(y) +'" ',
    'fill="rgb('+ str(r) +', '+ str(g) +', '+ str(b) +')">'
    '</rect>'
  ])

def rect_wx1px(x, y, w, r, g, b):
  # if r >= 254 and g >= 254 and b >= 254:
  #   return ''
  # color = '#' + hex(r)[2:4] + hex(g)[2:4] + hex(b)[2:4]
  return ''.join([
    '<rect width="'+ str(w) +'" height="'+ str(1) +'" ',
    'x="'+ str(x) +'" ',
    'y="'+ str(y) +'" ',
    'fill="rgb('+ str(r) +', '+ str(g) +', '+ str(b) +')">'
    '</rect>'
  ])

def svg_a(matrix):
  svg_body = []
  idx_row = 0
  for row in matrix:
    idx_col = 0
    for col in row:
      (r, g, b) = col
      svg_body.append(rect_1x1px(idx_col, idx_row, r, g, b))
      idx_col += 1
    idx_row += 1
  body = '\n'.join(svg_body)
  return '\n'.join([svg_head(matrix), body, svg_tail])

def svg_b(matrix):
  svg_body = []
  for idx_row, row in enumerate(matrix):
    rgb = [None, None, None]
    w_px = 0
    for idx_col, col in enumerate(row):
      (r, g, b) = col
      if idx_col == 0:
        rgb[0] = r
        rgb[1] = g
        rgb[2] = b
      if idx_col > 0 and r == rgb[0] and g == rgb[1] and b == rgb[2]:
        w_px += 1
      else:
        if rgb[0] is not None:
          rect = rect_wx1px(idx_col - w_px, idx_row, w_px + 1, rgb[0], rgb[1], rgb[2])
          if len(rect) > 0:
            svg_body.append(rect)
        rgb[0] = r
        rgb[1] = g
        rgb[2] = b
        w_px = 0
      if idx_col == len(row) - 1:
        if rgb[0] is not None:
          rect = rect_wx1px(idx_col - w_px, idx_row, w_px + 1, rgb[0], rgb[1], rgb[2])
          if len(rect) > 0:
            svg_body.append(rect)

  body = '\n'.join(svg_body)
  return '\n'.join([svg_head(matrix), body, svg_tail])