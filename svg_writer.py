import numpy as np

# TODO: naturalWidthを考慮すべき
def svg_head(mat, dpr=1):
  (height, width, depth) = np.shape(mat)
  return ''.join([
    '<svg xmlns="http://www.w3.org/2000/svg" '
    'width="' + str(width / dpr) + '" ',
    'height="' + str(height / dpr) + '" ',
    'viewBox="0 0 ' + str(width / dpr) + ' ' + str(height / dpr) + '">'
  ])

def rect_1px(x, y, r, g, b, dpr=1):
  p = 1 / dpr
  return ''.join([
    '<rect width="'+ str(p) +'" height="'+ str(p) +'" ',
    'x="'+ str(x) +'" ',
    'y="'+ str(y) +'" ',
    'fill="rgb('+ str(r) +', '+ str(g) +', '+ str(b) +')">'
    '</rect>'
  ])

svg_tail = '</svg>'

def svg_a(matrix, dpr=1):
  svg_body = []
  idx_row = 0
  for row in matrix:
    idx_col = 0
    for col in row:
      (r, g, b, a) = col
      svg_body.append(rect_1px(idx_col, idx_row, r, g, b, 1))
      idx_col += 1
    idx_row += 1
  body = '\n'.join(svg_body)
  return '\n'.join([svg_head(matrix, dpr), body, svg_tail])
