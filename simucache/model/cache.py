'''
Created on 14/05/2013

@author: diogo
'''

class Cache(object):
    '''
    Cache model. Here, some strategies like LRU, FIFO and RAND are implemented
    '''


    def __init__(self):
        '''
        List with files and there frequencies. Therefore, a strategy
        '''
        self.files = None
        self.strategy = 'FIFO'        