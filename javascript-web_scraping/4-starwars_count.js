#!/usr/bin/node
const request = require('request');
const process = require('process');
const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const api = JSON.parse(body);
    const films = api.results;
    let cameoCount = 0;
    for (let i = 0; i < films.length; i++) {
      for (let j = 0; j < films[i].characters.length; j++) {
        if (films[i].characters[j].includes('18')) {
          cameoCount += 1;
        }
      }
    }
    console.log(cameoCount);
  }
}
);
