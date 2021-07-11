'''RabbitMQ Consumer'''
from abc import ABC, abstractmethod
from .client import RabbitMQ


class RabbitMQConsumer(ABC, RabbitMQ):
    '''Consume messages from a RabbitMQ Queue'''

    @abstractmethod
    def callback(self, ch, method, properties, body):
        pass

    def consume(self):
        '''keep checking the queue'''
        self.channel.basic_consume(
            queue=self.queue, on_message_callback=self.callback, auto_ack=True)
        self.channel.start_consuming()
