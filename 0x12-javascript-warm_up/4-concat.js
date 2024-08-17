#!/usr/bin/node
// prints two args passed to it with the format: "is"

const args = process.argv.slice(2);

const firstArg = args[0]; // gets first argument

const secondArg = args[1]; // gets second argument

if (firstArg === undefined || secondArg === undefined) {
  console.log('No argument');
} else {
  console.log(firstArg + ' is ' + secondArg);
}
