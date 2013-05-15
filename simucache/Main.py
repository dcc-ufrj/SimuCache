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
    parser.add_argument("-e", "--epsilon", help="value of epsilon used to change frequencies. Could be a list with positive and negative values",
                    type=float, nargs='*')
    parser.add_argument("-i", "--increase_epsilon", help="number of the files that need epsilon increased",
                    type=int, nargs='*')
    parser.add_argument("-d", "--decrease_epsilon", help="number of the files that need epsilon decreased",
                    type=int, nargs='*')
    parser.add_argument("-c", "--cache_strategy", help="type of cache used. It could be: FIFO, RAND or LRU",
                    type=str)
    parser.add_argument("-cs", "--cache_size", help="size of the cache in integer",
                    type=int)
    parser.add_argument("-n", "--number_of_files", help="number of simulation files",
                    type=int)
    parser.add_argument("-t", "--timeslot", help="number of timeslots of the simulation",
                    type=int)
    parser.add_argument("-hi", "--hits", help="number of hits tries for each timeslot",
                    type=int)
    parser.add_argument("-l", "--list_of_frequencies", help="set individual frequencies for files and the values must sum 1",
                    type=float, nargs='*')
    arg = parser.parse_args()

    #This controller make the simulation
    if arg.simulation and not not arg.timeslot and not not arg.hits:
        simulation = main.Main(arg)
        simulation.run()
    #this controller handle the result
    if arg.result and not not arg.timeslot and not not arg.hits:
        result.Result(arg)
    #None set
    if not arg.result and not arg.simulation:
        print 'No args set. Please set --simulation and/or --result'
    
    if not arg.timeslot:
        print 'You need set at last 1 on --timeslot option'

    if not arg.hits:
        print 'You need set at last 1 on --hits option'