#!/usr/bin/node

const axios = require('axios');

const id = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${id}/`;

async function getCharacterNames() {
  try {
    // Fetch film data
    const filmResponse = await axios.get(url);
    const characters = filmResponse.data.characters;

    // Fetch and log character names
    for (const characterUrl of characters) {
      const characterResponse = await axios.get(characterUrl);
      console.log(characterResponse.data.name);
    }
  } catch (error) {
    console.error('Error:', error.message);
  }
}

getCharacterNames();
