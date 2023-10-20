const form = document.querySelector('form');
const output = document.querySelector('#output');

form.addEventListener('submit', (event) => {
  event.preventDefault();

  const dataText = form.elements['data_text'].value;
  const width = form.elements['width'].value;
  const height = form.elements['height'].value;
  const maxFontSize = form.elements['max_font_size'].value;
  output.innerHTML = "Loading responce...";
    
  const xhr = new XMLHttpRequest();
  xhr.open('POST', 'https://geog-nea-wordcloud.draggie.repl.co/generate_word_cloud');
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.onload = () => {
    if (xhr.status === 200) {
      output.innerHTML = `<img src="${xhr.response}" alt="Word Cloud">`;
    } else {
      output.innerHTML = 'Error generating word cloud';
    }
  };
  xhr.send(JSON.stringify({ data_text: dataText, width: width, height: height, max_font_size: maxFontSize }));
});