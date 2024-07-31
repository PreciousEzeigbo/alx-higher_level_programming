#!/usr/bin/node

const request = require('request');
const episodeNum = process.argv[2];
const API_URL = 'https://swapi-api.hbtn.io/api/films/';

// Make an HTTP GET request to the API with the episode number
request(API_URL + episodeNum, function (err, response, body) {
  if (err) {
    // If there's an error, log it
    console.log(err);
  } else if (response.statusCode === 200) {
    // If the request is successful, parse the JSON response
    const responseJSON = JSON.parse(body);
    // Print the title of the film
    console.log(responseJSON.title);
  } else {
    // If the request was unsuccessful, print the error code
    console.log('Error code: ' + response.statusCode);
  }
});
