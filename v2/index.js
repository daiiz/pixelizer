const u = 15
const fontSize = 13

const renderChar = char => {
  const canvas = document.querySelector('canvas.input')
  const dpr = window.devicePixelRatio
  const w = u * dpr
  const h = u * dpr
  canvas.width = w
  canvas.height = h
  const ctx = canvas.getContext('2d')
  ctx.clearRect()
  ctx.scale(dpr, dpr)
  canvas.style.width = `${u}px`
  canvas.style.height = `${u}px`

  ctx.fillStyle = 'brown'
  ctx.font = `bold ${fontSize}px sans-serif`
  ctx.textAlign = 'center'
  ctx.textBaseline = 'middle'
  ctx.fillText(char, w / (2 * dpr), h / (2 * dpr))
}

const readPixelColor = () => {
  const canvas = document.querySelector('canvas.input')
  const ctx = canvas.getContext('2d')
  const colorMap = []
  const colors = []
  for (let y = 0; y < canvas.height; y++) {
    for (let x = 0; x < canvas.height; x++) {
      if (x === 0) colorMap[y] = []
      const [r, g, b, a] = ctx.getImageData(x, y, 1, 1).data
      const color = `${r},${g},${b},${a / 255}` //a / 255
      if (r || g || b || a) {
        if (!colors.includes(color)) colors.push(color)
        colorMap[y].push(color)
      } else {
        colorMap[y].push(null)
      }
    }
  }
  // console.log(colors.length)
  // return renderPixel(colorMap)

  // 各行の先頭のピクセルカラー
  const headColors = colorMap.map(row => {
    for (const dot of row) {
      if (dot) return dot
    }
    return null
  })
  const headColorsNotNull = headColors.filter(color => !!color)
  for (let i = 0; i < headColors.length; i++) {
    if (!headColors[i]) {
      const r = Math.floor(Math.random() * (headColorsNotNull.length))
      headColors[i] = headColorsNotNull[r]
    }
  }

  // nullピクセルに着色する
  for (let y = 0; y < canvas.height; y++) {
    let prevColor = null
    for (let x = 0; x < canvas.width; x++) {
      prevColor = x === 0 ? headColors[y] : (colorMap[y][x - 1] || prevColor)
      if (!colorMap[y][x] && prevColor) colorMap[y][x] = prevColor
    }
  }
  renderPixel(colorMap)
}

const initCanvas = (canvas) => {
  const dpr = window.devicePixelRatio
  const w = u * dpr
  const h = u * dpr
  canvas.width = w
  canvas.height = h
  const ctx = canvas.getContext('2d')
  ctx.clearRect()
  canvas.style.width = `${u}px`
  canvas.style.height = `${u}px`
  return ctx
}

const renderPixel = (colorMap) => {
  const canvas = document.querySelector('canvas.output')
  const ctx = initCanvas(canvas)
  for (let y = 0; y < colorMap.length; y++) {
    const row = colorMap[y]
    for (let x = 0; x < row.length; x++) {
      const rgba = row[x]
      if (!rgba) continue
      ctx.fillStyle = `rgba(${rgba})`
      ctx.fillRect(x, y, 1, 1)
    }
  }
  const dpr = window.devicePixelRatio
  ctx.scale(dpr, dpr)

  const dataUrl = canvas.toDataURL('image/png')
  const img = document.createElement('img')
  img.className = 'res'
  img.src = dataUrl
  const imgs = document.querySelector('#imgs')
  imgs.appendChild(img)
}

window.addEventListener('load', e => {
  const text = document.querySelector('#char')
  text.addEventListener('keyup', e => {
    // const char = e.target.value
    // Enter以外無視
    const chars = (e.target.value).split('')
    if (e.keyCode !== 13 || !char) return
    // const chars = [char]
    for (let i = 0; i < 10; i++) chars.push('飯')
    const imgs = document.querySelector('#imgs')

    for (let i = 0; i < 10; i++) {
      for (const char of chars) {
        renderChar(char) // '##'
        readPixelColor()
      }
      const br = document.createElement('br')
      imgs.appendChild(br)
      console.log(i)
    }
  }, false)
}, false)

