#!/usr/bin/node

const process = require('process');
const argu = process.argv;
let count = 0;

if (argu !== null) {
	//for (let idx = 0; argu[idx] !== '/0'; idx++){
	//count++;
	for (idx in argu)
		count++;
  //}
}

if (count === 3 || count > 2) {
  console.log(argu[2]);
}

else if (count <= 2) {
  console.log('No Argument');
}
