'''
Created on 14/05/2013

@author: diogo
'''
from model.cache import Cache
from model.file import File
from model.frequency import Frequency
from model.log import Log
from random import choice, uniform
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
        self.epsilon = params.epsilon
        self.strategy = params.cache_strategy
        self.size = params.cache_size
        self.file_list = list()
        self.list_of_frequencies = params.list_of_frequencies
        self.timeslot = params.timeslot
        self.hits = params.hits
        self.log = Log(params)
        self.increase_epsilon = params.increase_epsilon
        self.decrease_epsilon = params.decrease_epsilon
        self.z = params.zipf_exponent
        
    def run(self):
        cache = Cache(self.size,self.strategy)
        self.gen_frequencies()
        self.gen_file_list()

        for timeslot in range(self.timeslot):
            self.go_time()
            self.apply_epsilon()
            for hits in range(self.hits):
                choice = self.select_file()
                response = cache.append_item(choice)
                if(response):
                    self.log.insert_log(response,timeslot+1,'hit',cache.get_file_status())
                else:
                    self.log.insert_log(choice,timeslot+1,'miss',cache.get_file_status())
        self.log.end_write()

    def gen_frequencies(self):
        if not self.list_of_frequencies and self.frequency == 'PERSONAL':
            print "You need a list of preferences"
        elif self.frequency != 'PERSONAL' and not not self.list_of_frequencies:
            print "You need to set preference to PERSONAL"
        else:
            if not self.list_of_frequencies:
                freq = Frequency(self.number,self.frequency,self.z)
            else:
                freq = Frequency(self.number,self.frequency,self.z,self.list_of_frequencies)
            freq.gen_frequency()
            self.list_of_frequencies = freq.frequency_
            
   
    def gen_file_list(self):
        for i in range(self.number):
            self.file_list.append(File(i,self.list_of_frequencies[i]))
    
    def select_file(self):
        limit = uniform(0,1)
        acum = 0
        helper_list = deepcopy(self.file_list)
        while acum <= limit:
            item = choice(helper_list)
            acum = item.frequency + acum
            helper_list.remove(item)
        for file_ in self.file_list:
            if file_.name == item.name:
                return file_
    
    def go_time(self):
        
        for file_ in self.file_list:
            file_.usage = file_.usage + 1
    
    def apply_epsilon(self):
        if not not self.epsilon:
            if len(self.epsilon) > 1:
                if self.is_not_negative_list():
                    for i in range(len(self.file_list)):
                        self.file_list[i].frequency = self.file_list[i].frequency + self.epsilon[i]
                
            elif not not self.increase_epsilon and not not self.decrease_epsilon:
                if self.is_not_negative_increase():
                    for file_ in self.file_list:
                        if file_.name in self.increase_epsilon:
                            file_.frequency = file_.frequency + self.epsilon[0]
                        else:
                            file_.frequency = file_.frequency - self.epsilon[0]
        
            else:
                length = len(self.file_list)
                if length % 2 == 0:
                    if self.is_not_negative_dual(self.epsilon[0],self.epsilon[0],length/2):
                        for file_ in self.file_list[:length/2]:
                            file_.frequency = file_.frequency - self.epsilon[0]
                        for file_ in self.file_list[length/2:]:
                            file_.frequency = file_.frequency + self.epsilon[0]
                else:
                    majority = int(length / 2) + 1
                    minority = majority - 1
                    divided = (self.epsilon[0]*minority)/majority
                    if self.is_not_negative_dual(divided,self.epsilon[0],majority):
                        for file_ in self.file_list[:majority]:
                            file_.frequency = file_.frequency - divided
                        for file_ in self.file_list[majority:]:
                            file_.frequency = file_.frequency + self.epsilon[0]

    def is_not_negative_list(self):
        counter = 0
        for i in range(len(self.file_list)):
            counter = counter + self.file_list[i].frequency  + self.epsilon[i]
            if self.file_list[i].frequency + self.epsilon[i] < 0:
                return False
        if counter == 1:
            return True
        else:
            return False
    
    def is_not_negative_dual(self,minus,max_,cut):
        counter = 0
        for file_ in self.file_list[:cut]:
            counter = counter + file_.frequency - minus
            if file_.frequency - minus < 0:
                return False
        for file_ in self.file_list[cut:]:
            counter = counter + file_.frequency + max_
            if file_.frequency + max_ < 0:
                return False
        if counter == 1:
            return True
        else:
            return False
                                
    def is_not_negative_increase(self):
        counter = 0
        for file_ in self.file_list:
            if file_.name in self.increase_epsilon:
                counter = counter + file_.frequency + self.epsilon[0]
                if file_.frequency + self.epsilon[0] < 0:
                    return False
            else:
                counter = counter + file_.frequency - self.epsilon[0]
                if file_.frequency - self.epsilon[0] < 0:
                    return False
        if counter == 1:
            return True
        else:
            return False