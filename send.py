#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello Techweber. Thanks for this useful tutorial!!')
print(" [x] Sent 'Hello Techweber. Thanks for this useful tutorial!'")
connection.close()