#!/usr/bin/node
const web_url = 'https://swapi-api.hbtn.io/api/films/?format=json'
$.getJSON(web_url, function(data) {
    const films = data.results
    for (const film of films)
    $("#list_movies").append('<li>' + film.title + '</li>')
})
