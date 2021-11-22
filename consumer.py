import pika

from admin.products.models import Product

params = pika.URLParameters('amqps://jejgzgvr:KwWWwFSO6r6dFFYR3mNixADW5PS1OBIS@gerbil.rmq.cloudamqp.com/jejgzgvr')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('Recieved in admin')
    print(body)

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print("started consuming......")

channel.start_consuming()

channel.close()
