from basicClient import BasicPikaClient

class BasicMessageReceiver(BasicPikaClient):

    def get_message(self, queue):
        method_frame, header_frame, body = self.channel.basic_get(queue)
        if method_frame:
            print(method_frame, header_frame, body)
            self.channel.basic_ack(method_frame.delivery_tag)
            return method_frame, header_frame, body
        else:
            print('No message returned')

    def consume_messages(self, queue):
            def callback(ch, method, properties, body):
                print(" [x] Received %r" % body)

                self.channel.basic_consume(queue=queue, on_message_callback=callback, auto_ack=True)

                print(' [*] Waiting for messages. To exit press CTRL+C')
                self.channel.start_consuming()

    def close(self):
        self.channel.close()
        self.connection.close()
      

if __name__ == "__main__":

    # Create Basic Message Receiver which creates a connection
    # and channel for consuming messages.
    basic_message_receiver = BasicMessageReceiver(
        "b-3d1a8932-19e2-41b9-9e6a-6f742d19df1c",
        "joaodanilo",
        "14S744w8!14S744w8!",
        "us-east-1"
    )
     # Consume the message that was sent.
    # basic_message_receiver.get_message("hello world queue")

    # Consume multiple messages in an event loop.
    basic_message_receiver.consume_messages("hello world queue")

    # Consume the message that was sent.
    basic_message_receiver.get_message("hello world queue")

    # Close connections.
    basic_message_receiver.close()

    