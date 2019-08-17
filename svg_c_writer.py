import numpy as np
from svg_writer import svg_head

def svg_c_head(mat):
  return ''.join([
    svg_head(mat, 6),
    '<foreignObject xmlns="http://www.w3.org/2000/svg" width="100%" height="100%" x="0" y="0">'
    '<html xmlns="http://www.w3.org/1999/xhtml">',
    '<style type="text/css">',
    '.dot {position: relative;font-size: 10px;width: 6px;height: 6px;margin: 0;padding: 0;display: inline-block;vertical-align: top; -webkit-font-smoothing: antialiased; font-weight:bold;} ',
    '.row {line-height: 6px; padding: 0; display: flex; width:100%;} ',
    '.main{position: relative;} ',
    '</style>',
    '<div class="main">'
  ])

svg_tail = '</div></html></foreignObject></svg>'

def rect_1x1px(r, g, b, px_str='@'):
  color = 'rgb('+ str(r) +', '+ str(g) +', '+ str(b) +')'
  colorT = 'rgb(' + str(r) + ', ' + str(g) + ', ' + str(b) + ', .8)'  # .5
  # text-shadow: 0px 0px 2px '+ colorT +';
  return '<span class="dot" style="color: ' + color + '; text-shadow: 0px 0px 2px ' + colorT + ';">' + px_str + '</span>'

def svg_c(matrix, px_str):
  body = []
  for idx_row, row in enumerate(matrix):
    body.append('<div class="row">')
    for idx_col, col in enumerate(row):
      (r, g, b) = col
      body.append(rect_1x1px(r, g, b, px_str))
    body.append('</div>')
  body = '\n'.join(body)
  return '\n'.join([svg_c_head(matrix), body, svg_tail])
