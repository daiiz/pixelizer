const loadRawImage = async imageName => {
  const res = await fetch(`/tmp/v2-2_${imageName}.txt`)
  const text = await res.text()
  const [info, body] = text.split('\n')
  try {
    return JSON.parse(body)
  } catch (err) {
    throw new Error('Invalid format!')
  }
}
