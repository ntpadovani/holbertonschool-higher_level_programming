#!/usr/bin/node
const request = require('request');
const process = require('process');
const url = process.argv[2];
request.get(url).on('response', function (res) {
  console.log('code:', res.statusCode);
});
