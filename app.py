import json
import pika
from flask import Flask, render_template
from flask_socketio import SocketIO
import threading
import time

# Configurações
RABBITMQ_URL = 'amqps://tndvsqvi:IDx8TigJOjKDeEqEaUM1qA4rt_t2MRmc@gorilla.lmq.cloudamqp.com/tndvsqvi'
QUEUE = 'temperatura'

latest_readings = []  # mantém um histórico curto para o front
MAX_HISTORY = 100

# Criação do app Flask e do SocketIO
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

def rabbit_consumer():
    params = pika.URLParameters(RABBITMQ_URL)
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE, durable=True)

    def callback(ch, method, properties, body):
        try:
            data = json.loads(body)
        except Exception as e:
            print('Erro parseando JSON:', e)
            ch.basic_ack(delivery_tag=method.delivery_tag)
            return

        # salva em memória
        latest_readings.append(data)
        if len(latest_readings) > MAX_HISTORY:
            latest_readings.pop(0)

        # emite para clientes conectados via socket
        socketio.emit('nova_leitura', data)

        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=QUEUE, on_message_callback=callback)
    print('Consumidor RabbitMQ rodando...')
    try:
        channel.start_consuming()
    except Exception as e:
        print('Consumidor finalizado:', e)
    finally:
        if connection and not connection.is_closed:
            connection.close()

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    # ao conectar, envia histórico curto
    socketio.emit('historico', latest_readings)

if __name__ == '__main__':
    # inicia thread do consumidor do RabbitMQ
    t = threading.Thread(target=rabbit_consumer, daemon=True)
    t.start()
    socketio.run(app, host='0.0.0.0', port=5000)
