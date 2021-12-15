#!/usr/bin/node
/* This is a a script that prints a message depending of the number of
arguments passed */
const myArgs = process.argv.slice(2);
if (myArgs[1] !== undefined) {
  console.log('Arguments found');
} else if (myArgs[0] !== undefined) {
  console.log('Argument found');
} else {
  console.log('No Argument');
}
