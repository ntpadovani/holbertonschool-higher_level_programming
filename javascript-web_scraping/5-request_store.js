#!/usr/bin/node
const request = require('request');
const process = require('process');
const fs = require('fs');
const url = process.argv[2];
const path = process.argv[3];
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const text = body;
    fs.writeFile(path, text, 'utf-8', function (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});
