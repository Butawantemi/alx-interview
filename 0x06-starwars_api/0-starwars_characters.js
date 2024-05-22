#!/usr/bin/node

const request = require('request');

const movieID = process.argv[2];
const movieURL = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

function sendRequest (characterList, index) {
  if (characterList.length === index) {
    return;
  }

  request(characterList[index], (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      console.log(JSON.parse(body).name);
      sendRequest(characterList, index + 1);
    }
  });
}

request(movieURL, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const characterList = JSON.parse(body).characters;

    sendRequest(characterList, 0);
  }
});