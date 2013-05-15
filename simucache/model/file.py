'''
Created on 14/05/2013

@author: diogo
'''
import sys
from random import uniform
class File(object):
    '''
    File model. All files are represented by it
    '''


    def __init__(self,frequency=0):
        '''
        Here set cache access frequency 0 to 1 and usage of file that increase with timeslot
        '''
        self.frequency = frequency
        self.usage = 0