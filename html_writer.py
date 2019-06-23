import numpy as np
from svg_writer import svg_head

def html_head(mat):
  return ''.join([
    # '<!doctype html>',
    # '<html>',
    # '<head>',
    # '<meta charset="utf-8" />',
    # '<link rel="stylesheet" href="./main.css" />',
    # '</head>',
    # '<body>',
    svg_head(mat, 6),
    '<foreignObject xmlns="http://www.w3.org/2000/svg" width="100%" height="100%" x="0" y="0">'
    '<html xmlns="http://www.w3.org/1999/xhtml">',
    # '<link rel="stylesheet" href="./main.css" />',
    '<style type="text/css">',
    '.dot {position: relative;font-size: 10px;width: 6px;height: 6px;margin: 0;padding: 0;display: inline-block;vertical-align: top; -webkit-font-smoothing: antialiased; font-weight:bold;} ',
    # '.dot-bg {width:5px; height:5px; top:0; left:0; display:block;position:absolute;}',
    '.row {line-height: 6px; padding: 0; display: flex; width:100%;} ',
    '.main{position: relative;} ',
    '</style>',
    '<div class="main">'
  ])

html_tail = '</div></html></foreignObject></svg>' #'</body></html>'

def rect_1x1px(r, g, b):
  color = 'rgb('+ str(r) +', '+ str(g) +', '+ str(b) +')'
  colorT = 'rgb('+ str(r) +', '+ str(g) +', '+ str(b) +', .8)' # .5
  # ■, ●, 飯, @, 新, 針
  # '<span class="dot" style="color: '+ color +'; text-shadow: -1px 0px 4px '+ colorT +';">車</span>'
  # return '<rect width="7" height="7" vector-effect="non-scaling-stroke" fill="'+ color +'"></rect>'
  return '<span class="dot" style="color: '+ color +'; text-shadow: 0px 0px 2px '+ colorT +';">0@</span>' # 針, text-shadow: -1px 0px 2px '+ colorT +';
  # <span class="dot-bg" style="background-color: '+ colorT +'"></span>

def html_a(matrix):
  body = []
  for idx_row, row in enumerate(matrix):
    body.append('<div class="row">')
    for idx_col, col in enumerate(row):
      (r, g, b) = col
      body.append(rect_1x1px(r, g, b))
    body.append('</div>')
  body = '\n'.join(body)
  return '\n'.join([html_head(matrix), body, html_tail])