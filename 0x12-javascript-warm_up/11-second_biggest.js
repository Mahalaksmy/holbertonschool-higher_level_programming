#!/usr/bin/node
/* Write a script that searches the second biggest integer in the list of arguments. */
const myArgs = process.argv.slice(2);
if (myArgs.length < 2) {
  console.log('0');
} else {
  myArgs.sort((a, b) => (b - a));
  console.log(myArgs[1]);
}
