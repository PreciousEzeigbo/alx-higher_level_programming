#!/usr/bin/node

// prints a square

const args = process.argv.slice(2);
const firstArg = args[0];
const num = parseInt(firstArg, 10);

if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    let line = '';
    for (let j = 0; j < num; j++) {
      line += 'X'; // Append X to the line
    }
    console.log(line);
  }
}
