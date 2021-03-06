from math import *
import numpy as np
import csv
import sys, getopt, cmath, os

def main(argv):
    if(len(sys.argv)<4):
        print "Usage readtimeandprint.py T0 FILENAME printFinfOrOrder"
        print "\tgenerated by script finfnmaxscript"
        print "\tintended to loop over times and produce a plot of"
        print "\tmax n used in generating finf, finf for each l, and time"
        print "\tprintFinfOrOrder is 1 for max order and 2 for Finf"
        exit()
    T0=int(sys.argv[1])
    filename=sys.argv[2]
    printFinfOrOrder=int(sys.argv[3])
    finfcolumn=3 #finfcolumn=2
    ordercolumn=1
    lcolumn=0
    
    datastruct=np.loadtxt(filename)
    outputpart1=np.array([T0])
    outputpart2=datastruct[:,printFinfOrOrder].transpose()
    output=np.append(outputpart1,outputpart2)
    print(", ".join(map(str,output)))
if __name__=="__main__":
    main(sys.argv[1:])
