#!/usr/bin/node
// prints the first argument passed

const args = process.argv.slice(2);
const first = args[0]; // gets the first argument

if (first !== undefined) {
  console.log(first);
} else {
  console.log('No argument');
}
