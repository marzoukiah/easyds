
  
import pika, json

params = pika.URLParameters('amqps://ldskdlgk:ghW99nsOB1ASfMqSWJNZOrs-7wbfSruw@baboon.rmq.cloudamqp.com/ldskdlgk')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)