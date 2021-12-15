#!/usr/bin/node
/* This a script that prints My number: <first argument converted in integer> if the first
argument can be converted to an integer */
const myArgs = process.argv[2];
if (parseInt(myArgs)) {
  console.log('My number: %d', parseInt(myArgs));
} else {
  console.log('Not a number');
}
