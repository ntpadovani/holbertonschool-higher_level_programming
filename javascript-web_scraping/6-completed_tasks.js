#!/usr/bin/node
const request = require('request');
const process = require('process');
const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const tasks = JSON.parse(body);
    const all = {};
    for (let i = 0; i < tasks.length; i++) {
      if (tasks[i].completed === true) {
        if (all[tasks[i].userId] === undefined) {
          all[tasks[i].userId] = 1;
        } else {
          all[tasks[i].userId]++;
        }
      }
    }
    console.log(all);
  }
});
