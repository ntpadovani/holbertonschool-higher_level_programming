#!/usr/bin/node
const fs = require('fs');
const process = require('process');
const filePath = process.argv[2];
fs.readFile(filePath, 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
