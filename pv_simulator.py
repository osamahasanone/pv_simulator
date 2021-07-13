import os
import sys
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
        self.__hours = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
        self.__powers = [0, 0.3, 0.8, 1.5, 2.3,
                         3, 3.2, 3.2, 3, 2.3, 1.5, 0.8, 0.3]

    @property
    def csv_path(self):
        return self.__csv_path

    @csv_path.setter
    def csv_path(self, csv_path):
        self.__csv_path = csv_path
        self.csv_helper = CSVHelper(path=csv_path)

    def current_pv_value(self, hour, minutes=0):
        '''predicate pv output power depending on time of the day

        @parameters:
        hour (int): hour of day (0-23)
        minutes (int): minutes after the hour
        '''
        if hour not in self.__hours:
            return 0
        if minutes == 0:
            return self.__powers[self.__hours.index(hour)]
        elif hour < 12:
            hour_power = self.__powers[self.__hours.index(hour)]
            next_hour_power = self.current_pv_value(hour+1, minutes=0)
            return round(hour_power + ((next_hour_power-hour_power)/60)*minutes, 2)
        elif hour >= 12:
            hour_power = self.__powers[self.__hours.index(hour)]
            next_hour_power = self.current_pv_value(hour+1, minutes=0)
            return round(hour_power - ((hour_power-next_hour_power)/60)*minutes, 2)

    def callback(self, ch, method, properties, body):
        '''To be called when a message detected in the queue'''
        received_watts = int(body)
        received_kw = round(received_watts/1000, 2)
        now = datetime.now()
        simulated_pv_kw = self.current_pv_value(
            hour=now.hour, minutes=now.minute)
        self.csv_helper.append_line(
            [now.strftime('%Y-%m-%d %H:%M:%S'), received_kw, simulated_pv_kw, round(received_kw+simulated_pv_kw, 2)])
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
