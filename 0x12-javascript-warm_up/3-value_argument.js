#!/usr/bin/node
/* This is a a script that prints the first argument passed to it */
const myArgs = process.argv.slice(2);
if (myArgs !== undefined) {
  console.log(myArgs);
} else {
  console.log('No Argument');
}
