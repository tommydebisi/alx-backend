import { createQueue } from 'kue';

const queue = createQueue();
const jobData = {
  phoneNumber: "0803",
  message: "Hello world",
}
const job = queue.create('push_notification_code', jobData);

job.on('failed', (errMessage) => {
  console.log('Notification job failed');
});

job.on('complete', (result) => {
  console.log('Notification job completed');
});

job.save((err) => {
  if (!err) {
    console.log(`Notification job created: ${job.id}`);
  }
});


