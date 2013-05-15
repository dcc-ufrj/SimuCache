'''
Created on 14/05/2013

@author: diogo
'''
from model.cache import Cache
from model.file import File
from model.frequency import Frequency
from random import choice, randint
from copy import deepcopy

class Main(object):
    '''
    Principal controller of the application
    '''


    def __init__(self,params):
        '''
        get application params
        '''
        self.number = params.number_of_files
        self.frequency = params.frequency
        self.strategy = params.cache_strategy
        self.file_list = list()
        self.list_of_frequencies = params.list_of_frequencies
        
    def main(self):
        cache = Cache(self.strategy)
        self.gen_frequencies()
        self.gen_file_list()
        cache.append_item(self.select_file())

    def gen_frequencies(self):
        if not self.list_of_frequencies and self.frequency == 'PERSONAL':
            print "You need a list of preferences"
        elif self.frequency != 'PERSONAL' and not not self.list_of_frequencies:
            print "You need to set preference to PERSONAL"
        else:
            frequency = Frequency(self.number,self.frequency,self.list_of_frequencies)
            self.list_of_frequencies = frequency.frequency
   
    def gen_file_list(self):
        for i in range(self.number-1):
            self.file_list.append(File(self.list_of_frequencies))
    
    def select_file(self):
        limit = randint(0,1)
        acum = 0
        helper_list = deepcopy(self.file_list)
        while acum <= limit:
            item = choice(helper_list)
            acum = item.frequency + acum
            helper_list.remove(item)