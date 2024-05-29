const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json'

fetch(url)
  .then(response => response.json())
  .then(data => {
    const character_name = data.name;
    const characterDiv = document.querySelector('#character');
    characterDiv.textContent = character_name;
  })
  .catch(error => {
    console.error('Error in fetching data', error);
  });
