'''
Created on 14/05/2013

@author: diogo
'''
import sys
from random import randint

class Cache(object):
    '''
    Cache model. Here, some strategies like LRU, FIFO and RAND are implemented
    '''


    def __init__(self,size,strategy='FIFO',files=list()):
        '''
        List with files and there frequencies. Therefore, a strategy
        '''
        self.files = files
        self.strategy = strategy
        self.size = size
    
    def run_strategy(self):
        if self.strategy == 'FIFO': self._fifo()
        elif self.strategy == 'RAND': self._rand()
        elif self.strategy == 'LRU': self._lru()
        else: self._error()
    
    def _error(self):
        print "No Valid Strategy"
        sys.exit()

    def _fifo(self):
        if not self.files:
            self.list.pop()
    
    def _rand(self):
        if not self.files:
            max_ = len(self.files)-1
            del self.files[randint(0,max_)]
    
    def _lru(self):
        if not self.files:
            max_usage = -1
            target = None
            for i in self.files:
                if (i.usage > max_usage):
                    max_usage = i.usage;
                    target = i
            if not not target: # if target exists
                self.files.remove(target)
    
    def append_item(self,item):
        if not not self.files:
            for element in self.files:
                if element.name == item.name:
                    return element
            
        if len(self.files) == self.size:
            self.run_strategy()
        self.files.insert(0, item)
        return False