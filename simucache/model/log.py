'''
Created on 14/05/2013

@author: diogo
'''
from os import path
from time import time

class Log(object):
    '''
    Log model. Writes all output from simulator
    '''


    def __init__(self,params):
        '''
        Here set the name of the file using params and time
        '''
        self.file_ = path.join('..','log',str(int(round(time() * 1000)))+".xml")
        self._params = vars(params);
        self._write_params()
         
    def _write(self):
        self.buffer = open(self.file_, 'a')
        self.buffer.write(self._str)
        self.buffer.close()
        self._str =''

    def insert_log(self,file_obj,timeslot,stats,cache):
        self._str = "<timeslot>{0}</timeslot> \
                    <name>{1}</name> \
                    <frequency>{2}</frequency> \
                    <usage>{3}</usage> \
                    <usage_frequency>{4}</usage_frequency> \
                    <stats>{5}</stats> ".format(str(timeslot),
                                                str(file_obj.name),
                                                str(file_obj.frequency),
                                                str(file_obj.usage),
                                                str(file_obj.freq_used),
                                                str(stats))
        self._write()
        self.cache = cache
        self._write_cache()    
    def _write_params(self):
        self._str = "<simulation><params>"
        for name in self._params:
            self._str = self._str + "<"+str(name)+">"+str(self._params[name])+"</"+str(name)+">"
        self._str = self._str + "</params><results>"
        self._write()
    
    def _write_cache(self):
        self._str = "<cache>"
        for item in self.cache:
            self._str = self._str + "<item>"
            for element in item:
                self._str = self._str + "<"+element+">"+item[element]+"</"+element+">"
            self._str = self._str + "</item>"
        self._str = self._str + "</cache>"
        self._write()
    
    def end_write(self):
        self._str = "</results></simulation>"
        self._write()