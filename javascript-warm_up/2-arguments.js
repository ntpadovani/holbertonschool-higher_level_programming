#!/usr/bin/node

const process = require('process');
const argu = process.argv;

if (argu.length === 2) {
  console.log('No argument');
}
if (argu.length === 3) {
  console.log('Argument found');
}
if (argu.length > 3) {
  console.log('Arguments found');
}
