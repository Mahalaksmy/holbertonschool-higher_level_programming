#!/usr/bin/node
const request = require("request");
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    let i = 0;

    for (const film of data.results) {
      for (const char of film.characters) {
        if (char.endsWith('18/')) {
          i++;
        }
      }
    }
    console.log(i);
  }
});
