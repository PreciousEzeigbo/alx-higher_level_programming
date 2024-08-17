#!/usr/bin/node

const args = process.argv.slice(2);

const firstArgs = args[0];

// convert the first argument to an integer
const convertedArg = parseInt(firstArgs, 10);

//check if conversion was successful
if (!isNaN(convertedArg)) {
	console.log('My nuber: ' + convertedArg);
}
else {
	console.log('Not a number');
}
