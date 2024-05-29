const url = 'https://swapi-api.hbtn.io/api/films/?format=json'

fetch(url)
  .then(res => res.json())
  .then(data => {
    const movies = data.results;
    const list_movies = document.querySelector('#list_movies');
    movies.forEach(movie => {
      const list_item = document.createElement('li');
      list_item.textContent = movie.title;
      list_movies.appendChild(list_item);
    });
  })
  .catch(error => {
    console.error('Error in fetching data', error);
  });
