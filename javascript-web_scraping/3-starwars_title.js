#!/usr/bin/node
const request = require('request');
const process = require('process');
const id = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${id}`;
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const film = JSON.parse(body);
    console.log(film.title);
  }
});
