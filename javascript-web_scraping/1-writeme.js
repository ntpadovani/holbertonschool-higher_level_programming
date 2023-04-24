#!/usr/bin/node
const fs = require('fs');
const process = require('process');
const filePath = process.argv[2];
const text = process.argv[3];
fs.writeFile(filePath, text, 'utf-8', function (err) {
  if (err) {
    console.log(err);
  }
});
