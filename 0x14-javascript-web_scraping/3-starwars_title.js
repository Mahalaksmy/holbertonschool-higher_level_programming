#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${id}`;

request(url, (err, body) => {
  if (err) throw err;
  const response = JSON.parse(body.toJSON().body);
  console.log(response.title);
});
