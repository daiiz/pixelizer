import numpy as np

svg_tail = '</svg>'

def svg_head(mat, dpr=1):
  (height, width, depth) = np.shape(mat)
  return ''.join([
    '<svg xmlns="http://www.w3.org/2000/svg" '
    'width="' + str(width / dpr) + '" ',
    'height="' + str(height / dpr) + '" ',
    'viewBox="0 0 ' + str(width / dpr) + ' ' + str(height / dpr) + '">'
  ])

def rect_1x1px(x, y, r, g, b, dpr=1):
  p = int(1 / dpr)
  return ''.join([
    '<rect width="'+ str(p) +'" height="'+ str(p) +'" ',
    'x="'+ str(x) +'" ',
    'y="'+ str(y) +'" ',
    'fill="rgb('+ str(r) +', '+ str(g) +', '+ str(b) +')">'
    '</rect>'
  ])

def rect_wx1px(x, y, w, r, g, b, dpr=1):
  return ''.join([
    '<rect width="'+ str(int(w / dpr)) +'" height="'+ str(int(1 / dpr)) +'" ',
    'x="'+ str(x) +'" ',
    'y="'+ str(y) +'" ',
    'fill="rgb('+ str(r) +', '+ str(g) +', '+ str(b) +')">'
    '</rect>'
  ])

def svg_a(matrix, dpr=1):
  svg_body = []
  idx_row = 0
  for row in matrix:
    idx_col = 0
    for col in row:
      (r, g, b, a) = col
      svg_body.append(rect_1x1px(idx_col, idx_row, r, g, b, 1))
      idx_col += 1
    idx_row += 1
  body = '\n'.join(svg_body)
  return '\n'.join([svg_head(matrix, dpr), body, svg_tail])

def svg_b(matrix, dpr=1):
  svg_body = []
  for idx_row, row in enumerate(matrix):
    rgb = [None, None, None]
    w_px = 0
    for idx_col, col in enumerate(row):
      (r, g, b, a) = col
      if idx_col == 0:
        rgb[0] = r
        rgb[1] = g
        rgb[2] = b
      if idx_col > 0 and r == rgb[0] and g == rgb[1] and b == rgb[2]:
        w_px += 1
      else:
        if rgb[0] is not None:
          svg_body.append(rect_wx1px(idx_col - w_px, idx_row, w_px + 1, rgb[0], rgb[1], rgb[2], 1))
        rgb[0] = r
        rgb[1] = g
        rgb[2] = b
        w_px = 0
      if idx_col == len(row) - 1:
        if rgb[0] is not None:
          svg_body.append(rect_wx1px(idx_col - w_px, idx_row, w_px + 1, rgb[0], rgb[1], rgb[2], 1))

  body = '\n'.join(svg_body)
  return '\n'.join([svg_head(matrix, dpr), body, svg_tail])