#!/usr/bin/node
/* This is a  a script that prints the addition of 2 integers */
function factorial (number) {
  if (!number) {
    return 1;
  } else {
    return number * factorial(number - 1);
  }
}
console.log(factorial(parseInt(process.argv[2])));
