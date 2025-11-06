import pika
import json
import time
import random

# remove espaços extras!
RABBITMQ_URL = 'amqps://tndvsqvi:IDx8TigJOjKDeEqEaUM1qA4rt_t2MRmc@gorilla.lmq.cloudamqp.com/tndvsqvi'
QUEUE = 'temperatura'

# conecta ao RabbitMQ
params = pika.URLParameters(RABBITMQ_URL)
connection = pika.BlockingConnection(params)
channel = connection.channel()

# garante que a fila existe
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
            properties=pika.BasicProperties(delivery_mode=2)  # mensagem persistente
        )
        print('Enviado:', payload)
        time.sleep(2)  # envia a cada 2 segundos
except KeyboardInterrupt:
    print('\nProducer finalizado.')
finally:
    connection.close()
