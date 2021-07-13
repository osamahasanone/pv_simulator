import sys
import time
import random
from rabbitmq.publisher import RabbitMQPublisher


class Meter(RabbitMQPublisher):
    '''produce messages to the broker with random values from 0 to 9000 Watts'''

    def current_value(self):
        return random.randint(0, 9000)

    def start(self, interval):
        '''keeps producing meassages every @interval

        @parameters:
        interval (int): seconds to wait after sending each watts value        
        '''
        try:
            while True:
                watts = self.current_value()
                self.publish(msg_body=str(watts))
                print(f' {watts} watts published to {self.queue} Queue')
                time.sleep(interval)
        except:
            self.close_connection()


if __name__ == '__main__':
    if len(sys.argv) != 4 or not sys.argv[3].isdigit():
        print('USAGE: python3 meter.py rabbitmq_server queue_name int_interval_seconds')
    else:
        print('---------------------------------------------------------------')
        print(
            f'Sending random "watts" values to PV Simulator every {sys.argv[3]} seconds')
        print('---------------------------------------------------------------')
        meter = Meter(server=sys.argv[1], queue=sys.argv[2])
        meter.start(interval=int(sys.argv[3]))
