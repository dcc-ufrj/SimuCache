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
    parser.add_argument("-f", "--frequency", help="type of frequency used. It could be: ",
                    type=str)
    parser.add_argument("-n", "--number_of_files", help="number of simulation files",
                    type=int)
    arg = parser.parse_args()

    #This controller make the simulation
    if (arg.simulation):
        main.Main(arg);
    #this controller handle the result
    if (arg.result):
        result.Result(arg);
    #None set
    if not arg.result and not arg.simulation:
        print 'No args set. Please set --simulation and/or --result'