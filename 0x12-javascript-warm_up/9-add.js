#!/usr/bin/node

// prints the addition of 2 integers

const args = process.argv.slice(2);

const firstArg = args[0];
const num1 = parseInt(firstArg, 10);

const secondArg = args[1];
const num2 = parseInt(secondArg, 10);

function add (a, b) {
  return a + b;
}
console.log(add(num1, num2));
