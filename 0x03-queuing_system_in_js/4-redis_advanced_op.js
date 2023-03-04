import { createClient, print } from 'redis';

const client = createClient();
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

const key = 'HolbertonSchools';

client.hset(key, { Portland: 50 }, print);
client.hset(key, { Seattle: 80 }, print);
client.hset(key, { "New York": 20 }, print);
client.hset(key, { Bogota: 20 }, print);
client.hset(key, { Cali: 40 }, print);
client.hset(key, { Paris: 2 }, print);

client.hgetall(key, (err, reply) => {
  if (err) {
    console.log(err);
  }
  console.log(reply);
})
