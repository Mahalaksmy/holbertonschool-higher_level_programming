#!/usr/bin/node
/* This is a that prints x times “C is fun */
const myArgs = process.argv[2];
if (myArgs > 0) {
  for (let i = myArgs; i; i--) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
