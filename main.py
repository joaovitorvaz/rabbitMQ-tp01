#!/usr/bin/env python
import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters("amqps://joaodanilo:14S744w8!14S744w8!@b-3d1a8932-19e2-41b9-9e6a-6f742d19df1c.mq.us-east-1.amazonaws.com:5671"))
channel = connection.channel()

channel.queue_declare(queue='hello')

messages = ["Primeira mensagem", "Segunda mensagem", "Terceira mensagem", "Quarta mensagem", "Quinta mensagem"];

for message in messages:
	channel.basic_publish(exchange='',
						  routing_key='hello',
						  body=message)
	print(" [x] Enviada '" + message + "'")
	time.sleep(1)

connection.close()