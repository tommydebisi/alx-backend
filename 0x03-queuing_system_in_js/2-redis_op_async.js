import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient();
  client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
  });

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

// client.connect();

const pSet = promisify(client.set);
const pGet = promisify(client.get);

async function setNewSchool(schoolName, value) {
  const res = await pSet(schoolName, value);

  res.then(print).catch((e) => {
    console.log(e);
  });
}

async function displaySchoolValue(schoolName) {
  const res = await pGet(schoolName);
  res.then((val) => {
    console.log(val);
  }).catch((err) => {
    console.log(err);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
