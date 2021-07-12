import os
import sys
import random
from datetime import datetime
from rabbitmq.consumer import RabbitMQConsumer
from filehelpers.csv_helper import CSVHelper


class PVSimulator(RabbitMQConsumer):
    '''listen to the broker for the meter values'''

    def __init__(self, server, queue, csv_path):
        '''Constructor

        @parameters:
        server (str): Server name or IP
        queue (str): Queue Name
        csv_path (str): full path to a CSV file
        '''
        super().__init__(server, queue)
        self.csv_path = csv_path
        self.csv_helper = CSVHelper(path=csv_path)

    @property
    def csv_path(self):
        return self.__csv_path

    @csv_path.setter
    def csv_path(self, csv_path):
        self.__csv_path = csv_path
        self.csv_helper = CSVHelper(path=csv_path)

    def current_pv_value(self):
        return random.randint(0, 9000)

    def callback(self, ch, method, properties, body):
        '''To be called when a message detected in the queue'''
        received_watts = int(body)
        received_kw = round(received_watts/1000, 2)
        simulated_pv_kw = round(self.current_pv_value()/1000, 2)
        self.csv_helper.append_line(
            [datetime.now().strftime('%Y-%m-%d %H:%M:%S'), received_kw, simulated_pv_kw, round(received_kw+simulated_pv_kw, 2)])
        print(f' {received_watts} watts dequeued from {self.queue} queue')

    def start(self):
        '''keep reading meassages til keyboard interrupt occurced'''
        try:
            pv_simulator.consume()
        except KeyboardInterrupt:
            print('Stopped by User')
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('USAGE: python3 pv_simulator.py rabbitmq_server queue_name file_name.csv')
    else:
        print('------------------------------------------------------------')
        print(f'Waiting for "watts" values from meter. To exit press CTRL+C')
        print('------------------------------------------------------------')
        pv_simulator = PVSimulator(
            server=sys.argv[1], queue=sys.argv[2], csv_path=sys.argv[3])
        pv_simulator.start()
