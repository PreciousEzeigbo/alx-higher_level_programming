#!/usr/bin/node

// Import the fs (File System) module
const fs = require('fs');

// The first argument is the file path
const file = process.argv[2];

// The second argument is the string to write
const content = process.argv[3];

// Write to the file asynchronously
fs.writeFile(file, content, 'utf-8', error => {
  if (error) {
    // Log any errors that occur
    console.log(error);
  }
});

