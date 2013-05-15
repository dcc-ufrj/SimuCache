'''
Created on 14/05/2013

@author: diogo
'''
import sys
from random import uniform, random
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
        self.frequency = frequency
    
    def gen_frequency(self):
        {'RANDOM': self._random(),
         'UNIFORM': self._uniform(),
         'PERSONAL': self._personal()
         }.get(self.frequency_type, self._error())()
    
    def _error(self):
        print "No Valid Frequency Type"
        sys.exit()
    
    def _random(self):
        max_value = 1
        for i in range(self.number -2):
            choice = random(0, max_value)
            self.frequency.append(choice)
            max_value = max_value - choice
            if max_value < 0:
                max_value = 0
        self.frequency.append(max_value)

    def _uniform(self):
        max_value = 1
        for i in range(self.number -2):
            choice = uniform(0, max_value)
            self.frequency.append(choice)
            max_value = max_value - choice
            if max_value < 0:
                max_value = 0
        self.frequency.append(max_value)
    
    def _personal(self):
        if len(self.frequency) != self.number:
            self._error()
        else:
            b = 0
            for i in self.frequency:
                b = b + i
            if b != 1:
                self._error()