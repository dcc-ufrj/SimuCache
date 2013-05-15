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
                    help="type of frequency used. For the last use --list_of_frequencies too.",
                    type=str, choices=['RANDOM', 'UNIFORM', 'PERSONAL'])
    parser.add_argument("-e", "--epsilon", help="value of epsilon used to change frequencies. Could be a list with positive and negative values",
                    type=float, nargs='*')
    parser.add_argument("-i", "--increase_epsilon", help="number of the files that need epsilon increased. Only work with pair --number_of_files",
                    type=int, nargs='*')
    parser.add_argument("-d", "--decrease_epsilon", help="number of the files that need epsilon decreased. Only work with pair --number_of_files",
                    type=int, nargs='*')
    parser.add_argument("-c", "--cache_strategy", help="type of cache used. It could be: FIFO, RAND, LRU or LFU",
                    type=str, choices=['FIFO', 'RAND', 'LRU', 'LFU'], required=True)
    parser.add_argument("-cs", "--cache_size", help="size of the cache in integer",
                    type=int, required=True)
    parser.add_argument("-n", "--number_of_files", help="number of simulation files",
                    type=int, required=True)
    parser.add_argument("-t", "--timeslot", help="number of timeslots of the simulation",
                    type=int, required=True)
    parser.add_argument("-hi", "--hits", help="number of hits tries for each timeslot",
                    type=int, required=True)
    parser.add_argument("-l", "--list_of_frequencies", help="set individual frequencies for files and the values must sum 1. Don't work with --increase_epsilon and --decrease_epsilon",
                    type=float, nargs='*')
    arg = parser.parse_args()

    if not arg.result and not arg.simulation:
        print 'No args set. Please set --simulation and/or --result'
    else:
        if arg.simulation:
            simulation = main.Main(arg)     #This controller make the simulation
            simulation.run()
    
        if arg.result:
            result.Result(arg) #this controller handle the result