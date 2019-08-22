// units
let u_w = 10 / 2 // 倍率: デモでは5,6,8,10くらいがいいい？
let u_h = u_w
// width, height dots
let w_dots = 1
let h_dots = 1
// flag for debug
let flag_debug = true

let fontSize = 12
let ctx = null
const colorMap = [[]]

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

const initColorMap = (width, height) => {

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
const drawChars = (ctx, { color, char, alpha } = {}) => {
  if (!char) char = '@'
  ctx.globalAlpha = alpha || 1
  for (let y = 0; y < h_dots; y++) {
    for (let x = 0; x < w_dots; x++) {
      if (!color) color = colorMap[y][x]
      ctx.fillStyle = color
      ctx.font = `bold ${fontSize}px sans-serif`
      ctx.textAlign = 'center'
      ctx.textBaseline = 'middle'
      const center = getCenter(x, y)
      ctx.fillText(char, center.x, center.y)
    }
  }
}

window.addEventListener('load', e => {
  w_dots = 100
  h_dots = 100
  ctx = initCanvas()
  main()
  bindEvents()
}, false)

const main = () => {
  if (!ctx) throw new Error('canvas is not initialized!')
  // drawLattice(ctx)
  drawChars(ctx, { color: 'green', char: '飯', alpha: .5 })
  // drawChars(ctx, { color: 'yellow', char: '井', alpha: .5 })
  // drawChars(ctx, { color: 'red', char: '@', alpha: .25 })
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
  document.querySelector('#btn_export').addEventListener('click', e => {
    const canvas = document.querySelector('#canvas')
    const dataUri = canvas.toDataURL('image/png')
    const a = document.querySelector('#download')
    a.href = dataUri
  })
}
