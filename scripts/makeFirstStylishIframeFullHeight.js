function makeFirstStylishIframeFullHeight() {
  const allStylishIframes = document.querySelectorAll(
    '.element-container > iframe[title="stylish_iframe.stylish_iframe"]'
  )
  const firstStylishIframe = allStylishIframes[0]

  firstStylishIframe.height = '100%'
  firstStylishIframe.parentElement.style.height = '100%'
}

console.log('this was injected')
makeFirstStylishIframeFullHeight()
window.addEventListener('message', function (e) {
  console.log('got an event of type: ', e.type)
  if (e.data.type === 'streamlit:render') {
    console.log('got streamlit:render message')
    makeFirstStylishIframeFullHeight()
  }
})
