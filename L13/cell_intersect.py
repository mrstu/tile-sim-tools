#!/usr/bin/env python

''''''

import os
import sys
import glob

from datetime import datetime
from datetime import timedelta

import argparse

import numpy as np

def readlist(listfile):
#     print listfile
    lf = open(listfile,'r')
    lf = lf.readlines()
#    for lfline in lf[:10]:
    filelist = []
    for lfline in lf:
        lfline = lfline.strip()
        filelist.append(lfline)
    return filelist

def read_snow(snowfile):
    lf = open(snowfile,'r')
    lf = lf.readlines()
#    for lfline in lf[:10]:
    celldb = {}
    for lfline in lf:
        lfline = lfline.rstrip()
#         cellno = lfline.split('\t')[0]
        cellpart=lfline.split('\t')[0]        
        cellno = cellpart.strip()
        celldb[cellno] = lfline
    return celldb

def read_veg(infile):
    lf = open(infile,'r')
    lf = lf.readlines()
#    for lfline in lf[:10]:
    celldb = {}
    vegdb = {}
    for lfline in lf:
        lfline = lfline.rstrip()
#         cellno = lfline.split('\t')[0]
        cellpart=lfline.split(' ')
        if len(cellpart) > 2:
            celldb[cellno].append(lfline)
        else:
            cellno = cellpart[0]
            vegdb[cellno] = cellpart[1]
            celldb[cellno] = []

    return celldb, vegdb

def main(*args):
    '''Extract select cells from VIC veg, snow bands files
    
    '''
#     print args
    
    usage = "usage: %prog [options] arg"
    parser = argparse.ArgumentParser(description='Return period start/ends with time range.')
    parser.add_argument("-i", "--indexfile",
                      dest="indexfile", default=None, help='List of grid cell numbers to extract.')
    parser.add_argument("-v", "--vegfile", dest="vegfile", default=None, help="Vegetation parameter file")
    parser.add_argument("-s", "--snowfile", dest="snowfile", default=None, help="Snow band elevation file")    

    args = parser.parse_args()

    indexfile = args.indexfile
    vegfile = args.vegfile    
    snowfile = args.snowfile    

    if os.path.exists(indexfile):
        inds = readlist(indexfile)
        if vegfile and os.path.exists(vegfile):
            celldb, vegdb = read_veg(vegfile)
            for ind in inds:
#                 print vegdb.keys()
#                 print vegdb
                print ind, vegdb[ind]
                for lv in celldb[ind]:
                    print lv
        if snowfile and os.path.exists(snowfile):
            celldb = read_snow(snowfile)
            for ind in inds:
                print celldb[ind]
    else:
        print 'No index file provided.'


if __name__=='__main__':
    main()
#     main(*sys.argv)