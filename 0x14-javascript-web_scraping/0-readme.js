#!/usr/bin/node

// Import the fs (File System) module
const fs = require('fs');

// The first argument passed to the script is the file path
const file = process.argv[2];

// Read the file asynchronously
fs.readFile(file, 'utf-8', (error, data) => {
  if (error) {
    // Handle errors (e.g., file not found, permission issues)
    console.error('Error reading file:', error);
    return;
  }
  // Print the content of the file to the console
  console.log(data);
});
