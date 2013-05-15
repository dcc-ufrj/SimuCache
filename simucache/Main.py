'''
Created on 11/10/2012

@author: diogo
'''

from controller import main, result
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--simulation", help="turn simulation mode on",
                    action="store_true")
    parser.add_argument("-r", "--result", help="turn result mode on",
                    action="store_true")
    parser.add_argument("-f", "--frequency",
                    help="type of frequency used. It could be: RANDOM, UNIFORM and PERSONAL. For the last use --list_of_frequencies too.",
                    type=str)
    parser.add_argument("-e", "--epsilon", help="value of epsilon used to change frequencies",
                    type=float)
    parser.add_argument("-c", "--cache_strategy", help="type of cache used. It could be: FIFO, RAND or LRU",
                    type=str)
    parser.add_argument("-n", "--number_of_files", help="number of simulation files",
                    type=int)
    parser.add_argument("-l", "--list_of_frequencies", help="set individual frequencies for files and the values must sum 1",
                    type=float, nargs='*')
    arg = parser.parse_args()

    #This controller make the simulation
    if (arg.simulation):
        main.Main(arg);
    #this controller handle the result
    if (arg.result):
        result.Result(arg);
    #None set
    if not arg.result and not arg.simulation:
        print arg
        print 'No args set. Please set --simulation and/or --result'