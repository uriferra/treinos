const express = require('express');
const app = express();
const bodyParser = require('body-parser');
app.use(bodyParser.json());
const cors = require('cors');
app.use(cors());

const messageRouter = require('./routes/message');
const get = require('./routes/get');

app.use('/', messageRouter);
app.use('/', get)

app.listen(3000, () => {
  console.log('Server running on port 3000');
});
