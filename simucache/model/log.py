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
        self.file_ = path.join('..','log',str(int(round(time() * 1000))))
        self._str = "Simulation Params: "+str(vars(params))+"\n";
        self._write()
        self._str = "Name;Frequency;Usage;Usage Frequency;Stats;Cache Items;Timeslot \n"
        self._write()
         
    def _write(self):
        self.buffer = open(self.file_, 'a')
        self.buffer.write(self._str)
        self.buffer.close()

    def insert_log(self,file_obj,timeslot,stats,cache):
        self._str = str(file_obj.name)+';'+str(file_obj.frequency)+';'+str(file_obj.usage)+';'+str(file_obj.freq_used)+';'+stats+';'+cache+';'+str(timeslot)+"\n"
        self._write()    