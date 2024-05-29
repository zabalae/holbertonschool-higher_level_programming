const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

fetch(url)
  .then(response => response.json())
  .then(data => {
    const hello_value = data.hello;
    const helloDiv = document.querySelector('#hello');
    helloDiv.textContent = hello_value;
  })
