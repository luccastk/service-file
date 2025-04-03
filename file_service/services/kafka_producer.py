# services/kafka_producer.py

from confluent_kafka import Producer
import json
import logging

class KafkaProducerService:
    def __init__(self, bootstrap_servers='localhost:9092'):
        self.producer = Producer({
            'bootstrap.servers': bootstrap_servers,
            'linger.ms': 10,
            'acks': 'all',
        })

    def _delivery_report(self, err, msg):
        if err is not None:
            logging.error(f"❌ Kafka erro: {err}")
        else:
            logging.info(f"✅ Kafka enviado: {msg.topic()} [{msg.partition()}] offset {msg.offset()}")

    def send(self, topic: str, value: dict, key: str = None):
        try:
            serialized_value = json.dumps(value).encode('utf-8')
            serialized_key = key.encode('utf-8') if key else None

            self.producer.produce(
                topic=topic,
                value=serialized_value,
                key=serialized_key,
                callback=self._delivery_report
            )
            self.producer.flush()
        except Exception as e:
            logging.exception(f"Erro ao produzir evento no tópico {topic}: {e}")
