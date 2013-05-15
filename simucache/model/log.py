'''
Created on 14/05/2013

@author: diogo
'''
from time import gmtime, strftime
from os import path

class Log(object):
    '''
    Log model. Writes all output from simulator
    '''


    def __init__(self,params):
        '''
        Here set the name of the file using params and time
        '''
        self.file_ = path.join('..','log',str(params)+strftime("%d-%m-%Y_%H:%M:%S", gmtime()))
         
    def _write(self):
        self.buffer = open(self.file_, 'a')
        self.buffer.write(self._str)
        self.buffer.close()

    def insert_log(self,file_obj,timeslot):
        self._str = str(file_obj.name)+';'+str(file_obj.frequency)+';'+str(file_obj.usage)+';'+str(timeslot)+"\n"
        self._write()    