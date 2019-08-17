const fs = require('fs')
const puppeteer = require('puppeteer')

const main = async url => {
  const browser = await puppeteer.launch({ headless: true })
  const page = await browser.newPage()
  await page.goto(url, {
    timeout: 1200 * 1000,
    waitUntil: 'domcontentloaded'
  })
  await page.waitFor(300)
  console.log('done!')
  const range = await page.evaluate(selector => {
    const svg = document.querySelector(selector)
    const { left: x, top: y, width, height } = svg.getBoundingClientRect()
    return { x, y, width, height }
  }, 'svg')
  console.log(range)
  await page.setViewport({
    width: range.width,
    height: range.height,
    deviceScaleFactor: 1
  })
  await page.waitFor(300)
  const filePath = './pptr/a.png'
  const buf = await page.screenshot({
    clip: range,
    path: filePath
  })
  await browser.close()
}

main('http://localhost:8000/html/pancake.a.svg')
