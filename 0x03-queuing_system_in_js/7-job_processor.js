import { createQueue } from "kue";

const blackListed = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done)
