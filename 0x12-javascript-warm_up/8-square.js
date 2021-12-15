#!/usr/bin/node
/* This is a script that prints a square */
const myArgs = process.argv[2];
if (myArgs > 0) {
  for (let i = 0; i < myArgs; i++) {
    console.log('X'.repeat(myArgs));
  }
} else {
  console.log('Missing size');
}
