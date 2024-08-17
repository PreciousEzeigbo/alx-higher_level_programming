#!/usr/bin/node
//  prints a message depending on the number of arg

const args = process.argv.slice(2); // skip the filename and file path

if (args.length === 0) {
  console.log('No argument');
} else if (args.length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
