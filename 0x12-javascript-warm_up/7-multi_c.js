#!/usr/bin/node

// prints x times "C is fun"

const args = process.argv.slice(2);
const firstArg = args[0];
const num = parseInt(firstArg, 10);

// Check if the argument can be converted to a valid integer
if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
}
