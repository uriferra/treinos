const express = require('express');
const connection = require('/Users/uriel/Downloads/testbackend/config/db');
const router = express.Router();


router.post('/send-message', (req, res) => {
  const message = req.body.message;

  connection.query('INSERT INTO messages (content) VALUES (?)', [message], function(error, results, fields) {
    if (error) {
      console.log(error);
      res.status(500).send('Error saving message');
    } else {
      console.log(results);
      res.status(200).send('Message saved successfully');
    }
  });
});

module.exports = router;
