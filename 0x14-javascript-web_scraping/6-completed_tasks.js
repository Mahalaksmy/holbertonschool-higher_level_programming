#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (err, resp, body) => {
  if (err) throw err;

  const data = {};
  const todo = JSON.parse(body);

  for (let i = 0; i < todo.length; i++) {
    const user_Id = todo[i].user_Id;
    const taskStatus = todo[i].completed;

    if (taskStatus === true) {
      if (!data[user_Id]) {
        data[user_Id] = 1;
      } else {
        data[user_Id] += 1;
      }
    }
  }
  console.log(data);
});
