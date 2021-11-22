import pika, json

params = pika.URLParameters('amqps://jejgzgvr:KwWWwFSO6r6dFFYR3mNixADW5PS1OBIS@gerbil.rmq.cloudamqp.com/jejgzgvr')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)
