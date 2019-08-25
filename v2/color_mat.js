// return new matrix

// 色のRGB距離
const d = (rgb1, rgb2) => {
  return 1
}

const getEmptyMat = (wDots, hDots) => {
  const mat = []
  for (let y = 0; y < hDots; y++) {
    mat.push([])
    for (let x = 0; x < wDots; x++) {
      mat[y][x] = '0,0,0'
    }
  }
  return mat
}

// タイル化する
// wDots x hDots の矩形範囲を平均色化する
const tile = (rawMat, wDots=1, hDots=1) => {
  const yLen = rawMat.length
  const xLen = rawMat[0].length
  const mat = getEmptyMat(xLen, yLen)
  for (let y = 0; y < yLen; y += hDots) {
    for (let x = 0; x < xLen; x += wDots) {
      // (x, y): タイル矩形の左上座標
      paintTile(mat, rawMat, { x, y, w: wDots, h: hDots })
    }
  }
  // console.log(mat)
  return mat
}

// matの一部分を着色する
const paintTile = (mat, rawMat, tileInfo) => {
  const yLen = rawMat.length
  const xLen = rawMat[0].length
  const tileW = Math.min(tileInfo.w, xLen - tileInfo.x)
  const tileH = Math.min(tileInfo.h, yLen - tileInfo.y)
  const tileDots = tileW * tileH
  // 平均色を取得する
  const colors = []
  let aveColor = [0, 0, 0]
  try {
    for (let y = 0; y < tileH; y++) {
      for (let x = 0; x < tileW; x++) {
        const rgb = rawMat[tileInfo.y + y][tileInfo.x + x]
        const [r, g, b] = rgb.split(',').map(c => +c.trim())
        aveColor[0] += r
        aveColor[1] += g
        aveColor[2] += b
        colors.push([r, g, b])
      }
    }
  } catch (err) {
    console.error(err)
    return
  }
  aveColor = aveColor.map(c => Math.floor(c / tileDots))
  // matを着色する
  for (let y = 0; y < tileH; y++) {
    for (let x = 0; x < tileW; x++) {
      const aveRgb = aveColor.join(',')
      mat[tileInfo.y + y][tileInfo.x + x] = aveRgb
    }
  }
}
