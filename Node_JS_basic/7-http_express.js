const express = require('express');
const fs = require('fs');

const app = express();
const PORT = 1245;
const database = process.argv[2];

const countStudents = (path) => new Promise((resolve, reject) => {
  fs.readFile(path, 'utf8', (err, data) => {
    if (err) {
      reject(new Error('Cannot load the database'));
      return;
    }

    const lines = data
      .trim()
      .split('\n')
      .filter((line) => line);

    const students = lines.slice(1);

    const fields = {};
    students.forEach((line) => {
      const [firstname, , , field] = line.split(',');
      if (!fields[field]) fields[field] = [];
      fields[field].push(firstname);
    });

    let output = `Number of students: ${students.length}\n`;
    for (const field of Object.keys(fields)) {
      output += `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}\n`;
    }

    resolve(output.trim());
  });
});

/**
 * ROUTES
 */
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  res.write('This is the list of our students\n');
  try {
    const result = await countStudents(database);
    res.end(result);
  } catch (error) {
    res.end(error.message);
  }
});

app.listen(PORT);

module.exports = app;
