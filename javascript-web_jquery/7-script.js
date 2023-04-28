#!/usr/bin/node
const web_url = 'https://swapi-api.hbtn.io/api/people/5/?format=json'
$.getJSON(web_url, function(character) {
    $("#character").append(character.name)
})
