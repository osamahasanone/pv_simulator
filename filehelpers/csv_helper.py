'''CSV operations abstraction'''
import os
import csv


class CSVHelper:
    '''CSV file helper'''

    def __init__(self, path):
        '''Constructor: if file not existed, it will be created along with headers

        @parameters:
        path (str): full path to a CSV file
        '''
        self.path = path
        if not os.path.exists(path):
            self.append_line(['TS', 'meter', 'pv_simulated', 'sum'])

    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, value):
        self.__path = value

    def __str__(self):
        return self.path

    def append_line(self, values):
        '''Append line to a CSV file

        @parameters:
        values (list): values of the line
        '''
        with open(self.path, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(values)
