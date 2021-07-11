'''RabbitMQ Publisher'''
from .client import RabbitMQ


class RabbitMQPublisher(RabbitMQ):
    '''Publish messages to a RabbitMQ Queue'''

    def publish(self, msg_body):
        '''publish one message

        @parameters:
        msg_body (str): Message body
        '''
        self.channel.basic_publish(
            exchange='', routing_key=self.queue, body=msg_body)
