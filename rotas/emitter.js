// File with the functions to send messages

const amqplib = require('amqplib');
const { execute } = require('../examples/crawl');

const exchangeName = 'direct_tweets';

const args = process.argv.slice(2);
const messenger = {};

if(args[0] === 'crawler') {
  messenger.port = args[1];
  messenger.usersArray = args[2].split(' ');
  messenger.amount = args[3];

} else {
  messenger.port = args[1];
  messenger.routingKey = args[2];
  messenger.msg = args[3] || 'No message';
}

console.log(messenger);

const sendMsg = async () => {
  try {
    const url = messenger.port && messenger.port.length === 4 ? connect(messenger.port) : localhost();

    const connection = await amqplib.connect(url);
    const channel = await connection.createChannel();
    await channel.assertExchange(exchangeName, 'direct', { durable: true });
  
    if (messenger.msg) {
      channel.publish(exchangeName, messenger.routingKey, Buffer.from(messenger.msg));
      console.log("\x1b[36m%s\x1b[0m", 'Sent: ', messenger.msg);
  
      setTimeout(() => {
        connection.close();
        process.exit(0);
      }, 500)
  
    } else {
      const arrayMsg = await execute(messenger.usersArray, messenger.amount);
  
      arrayMsg.forEach(msg => {
        channel.publish(exchangeName, msg.screenName, Buffer.from(msg.text));
        console.log("\x1b[36m%s\x1b[0m", 'Sent: ', msg.text);
      });
  
      setTimeout(() => {
        connection.close();
        process.exit(0);
      }, 500)
    }
  } catch(error) {
    console.error(error)
  }
}

const connect = (port) => {
  return `amqp://admin:admin@0.0.0.0:${port}`;
}

const localhost = () => {
  return `amqp://localhost`;
}

sendMsg();
