'''
Created on 14/05/2013

@author: diogo
'''
import sys
from random import uniform
class Frequency(object):
    '''
    Frequency model. Generate file frequencies
    '''


    def __init__(self,number_files,frequency_type='RANDOM',frequency=list()):
        '''
        Here set cache access frequency type and number of files
        '''
        self.frequency_type = frequency_type
        self.number = number_files
        self.frequency_ = frequency
    
    def gen_frequency(self):
        if self.frequency_type == 'RANDOM': self._random()
        elif self.frequency_type == 'UNIFORM': self._uniform()
        elif self.frequency_type == 'PERSONAL': self._personal()
        else: self._error()
    
    def _error(self):
        print "No Valid Frequency Type"
        sys.exit()
    
    def _random(self):
        max_value = 1
        for i in range(self.number -1):
            choice = uniform(0, max_value)
            self.frequency_.append(choice)
            max_value = max_value - choice
            if max_value < 0:
                max_value = 0
        self.frequency_.append(max_value)

    def _uniform(self):
        frequency = float(1)/float(self.number)
        for i in range(self.number):
            self.frequency_.append(frequency)
    
    def _personal(self):
        if len(self.frequency_) != self.number:
            self._error()
        else:
            b = 0
            for i in self.frequency_:
                b = b + i
            if b != 1:
                self._error()