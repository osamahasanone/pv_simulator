
'''basic behaviour of RabbitMQ publisher and Consumer'''


import pika


class RabbitMQ:
    '''Establish and close connection to RabbitMQ server'''

    def __init__(self, server, queue):
        '''Establish the connection

        @parameters:
        server (str): Server name or IP
        queue (str): Queue Name
        '''
        self.server = server
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(server))
        self.channel = self.connection.channel()
        self.queue = queue
        self.channel.queue_declare(queue=queue)

    def close_connection(self):
        '''close RabbitMQ Connection'''
        self.connection.close()
