import { createClient } from 'redis';

const client = createClient();

client.on('message', function (channel, message) {
  if (channel === 'holberton school channel') {
    if (message === 'KILL_SERVER') {
      client.unsubscribe(channel);
      client.quit();
    } else {
      console.log(message);
    }
  }
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

// client.connect();
client.subscribe('holberton school channel');
