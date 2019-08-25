// units
let u_w = 10 / 2 // 倍率: デモでは5,6,8,10くらいがいいい？
let u_h = u_w
// width, height dots
let w_dots = 1
let h_dots = 1
// flag for debug
let flag_debug = true

let fontSize = 10.5 //12 - 2
let ctx = null
let colorType = 'rgb'
let colorMat = [[]]
let rawImageName = 'pancake.100'
let rawImageExt = 'jpg'

const initCanvas = () => {
  const canvas = document.querySelector('#canvas')
  const dpr = window.devicePixelRatio
  const w = (u_w * w_dots) * dpr
  const h = (u_h * h_dots) * dpr
  canvas.width = w
  canvas.height = h
  const ctx = canvas.getContext('2d')
  ctx.clearRect(0, 0, w, h)
  canvas.style.width = `${u_w * w_dots}px`
  canvas.style.height = `${u_h * h_dots}px`
  ctx.scale(dpr, dpr)
  return ctx
}

const initColorMat = async () => {
  const rgbMat = await loadRawImage(rawImageName)
  const yLen = rgbMat.length
  const xLen = rgbMat[0].length
  colorType = rgbMat[0][0].length === 4 ? 'rgba' : 'rgb'
  for (let y = 0; y < yLen; y++) {
    for (let x = 0; x < xLen; x++) {
      const [r, g, b] = rgbMat[y][x]
      rgbMat[y][x] = `${r},${g},${b}`
    }
  }
  colorMat = rgbMat
  return { widthDots: xLen, heightDots: yLen }
}

// y行x粒目の中心座標
const getCenter = (x, y) => {
  const offsetX = u_w * x
  const offsetY = u_h * y
  return {
    x: offsetX + (u_w / 2),
    y: offsetY + (u_h / 2)
  }
}

// 格子を描画
// center
const drawLattice = (ctx, { color } = {}) => {
  for (let y = 0; y < h_dots; y++) {
    for (let x = 0; x < w_dots; x++) {
      if (flag_debug) {
        const offsetX = u_w * x
        const offsetY = u_h * y
        ctx.strokeStyle = '#ccc'
        ctx.strokeRect(offsetX, offsetY, u_w, u_h)
      }
      const center = getCenter(x, y)
      ctx.fillStyle = color || 'blue'
      ctx.fillRect(center.x - 1, center.y - 1, 2, 2)
    }
  }
}

// 文字を描画
// center
const drawChars = (ctx, { color, mat, char, alpha, blur } = {}) => {
  // if (!char) char = '@'
  ctx.globalAlpha = alpha || 1
  const fillColorMat = mat || colorMat
  let fillColor = color
  for (let y = 0; y < h_dots; y++) {
    for (let x = 0; x < w_dots; x++) {
      if (!color) fillColor = `${colorType}(${fillColorMat[y][x]})`
      ctx.fillStyle = fillColor
      ctx.font = `900 ${fontSize}px sans-serif`
      ctx.textAlign = 'center'
      ctx.textBaseline = 'middle'
      if (blur) {
        ctx.shadowColor = fillColor
        ctx.shadowBlur = 1
      } else {
        ctx.shadowBlur = 0
      }
      const center = getCenter(x, y)
      ctx.fillText(char, center.x, center.y)
      // ctx.fillRect(u_w * x, u_w * y, u_w, u_h)
    }
  }
}

window.addEventListener('load', async e => {
  const size = await initColorMat()
  w_dots = size.widthDots
  h_dots = size.heightDots
  ctx = initCanvas()
  main()
  bindEvents()
}, false)

const main = () => {
  // 均等透過
  const drawWithAutoAlpha = options => {
    const _alpha = 1 / options.length
    for (const option of options) {
      const char = option.char
      const mat = option.mat
      const alpha = option.alpha || _alpha
      drawChars(ctx, { mat, char, alpha })
      if (flag_debug) console.log(char, alpha)
    }
  }
  if (!ctx) throw new Error('canvas is not initialized!')
  // drawLattice(ctx)
  drawWithAutoAlpha([
    // { char: '■', mat: tile(colorMat, 10, 10) },
    { char: '■', mat: tile(colorMat, 4, 4), alpha: .1 },
    { char: '■', mat: tile(colorMat, 2, 2), alpha: .1 }
  ])
  drawWithAutoAlpha([
    { char: '飯' },
    { char: '@' },
    { char: '~' },
  ])
  updatePreview()
  // drawChars(ctx, { color: 'green', char: '飯', alpha: .5 })
}

const bindEvents = () => {
  // 倍率変更して再描画
  document.querySelector('#redraw').addEventListener('click', e => {
    const value = +document.querySelector('#x').value
    u_w = value
    u_h = value
    ctx = initCanvas()
    main()
  }, false)
  // PNG画像としてダウンロード
  document.querySelector('#btn_export').addEventListener('click', updatePreview)
}

const updatePreview = () => {
  const canvas = document.querySelector('#canvas')
  const dataUri = canvas.toDataURL('image/png')
  const a = document.querySelector('#download')
  a.href = dataUri
  // Preview
  const x = 3
  const style = `width: ${w_dots * x}px; height: ${h_dots * x}px;`
  const imgX2 = document.querySelector('#img-x2')
  imgX2.style = style
  imgX2.src = dataUri
  const imgX2Raw = document.querySelector('#img-x2-raw')
  imgX2Raw.style = style
  imgX2Raw.src = getRawImageSrcUrl(rawImageName, rawImageExt)

  const container = document.querySelector('#container')
  container.style = `height: ${h_dots * x}px`
  $("#container").twentytwenty({
    no_overlay: true,
    click_to_move: true
  })
}
