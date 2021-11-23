import pika, json

params = pika.URLParameters('amqps://dpubrmwx:dBAPxZ969vFJxH98CWyCkV4WAD2jPSpu@vulture.rmq.cloudamqp.com/dpubrmwx')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)