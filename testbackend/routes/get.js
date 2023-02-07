const express = require('express');
const connection = require('/Users/uriel/Downloads/testbackend/config/db');

const get = express.Router();

app.get('/get-messages', (req, res) => {
    connection.query('SELECT * FROM messages', (error, results) => {
      if (error) throw error;
      res.json(results);
    });
  });

  module.exports = get;