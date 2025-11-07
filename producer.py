import pika
import json
import time
import random

RABBITMQ_URL = 'amqps://tndvsqvi:IDx8TigJOjKDeEqEaUM1qA4rt_t2MRmc@gorilla.lmq.cloudamqp.com/tndvsqvi'
QUEUE = 'temperatura'

params = pika.URLParameters(RABBITMQ_URL)
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue=QUEUE, durable=True)

try:
    while True:
        temp = round(random.uniform(20.0, 35.0), 2)
        payload = {
            'sensor_id': 'sensor-01',
            'timestamp': int(time.time()),
            'temperature': temp
        }
        channel.basic_publish(
            exchange='',
            routing_key=QUEUE,
            body=json.dumps(payload),
            properties=pika.BasicProperties(delivery_mode=2) 
        )
        print('Enviado:', payload)
        time.sleep(2)
except KeyboardInterrupt:
    print('\nProducer finalizado.')
finally:
    connection.close()
