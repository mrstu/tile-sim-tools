#!/usr/bin/env python

''''''

import os
import sys
import glob

import argparse

def main(*args):
    '''Extract select cells from VIC veg, snow bands files
    
    '''
#     print args
    
    usage = "usage: %prog [options] arg"
    parser = argparse.ArgumentParser(description='Return period start/ends with time range.')
    parser.add_argument("-r", "--rowindexfile",
                      dest="frows", default=None, help='List of row indices (zero-based, ascending order) to extract')
    parser.add_argument("-t", "--targetfile", dest="target", default=None, help="Input file")
    parser.add_argument("-o", "--outputfile", dest="outfile", default=None, help="Truncated file")    

    args = parser.parse_args()

    indexfile = open(args.frows,'rb')
#     target = args.target
    outfile = open(args.outfile,'wb')    
    
    rownums=[int(line.rstrip()) for line in indexfile.readlines()]
    indexfile.close()
#     print rownums
    nline=0
    rcounter=0
    nselect=len(rownums)
    with open(args.target) as fp:
        for line in fp:
    #         txt = line.rstrip()
#             print nline, len(rownums), rcounter, line

            if rcounter < nselect and nline == rownums[rcounter]:
#                 print 'nline', nline, rownums[rcounter], rcounter
                outfile.write(line)
                rcounter+=1
            nline+=1
    print len(rownums)
    outfile.close()
#     target.close()

if __name__=='__main__':
#     main()
    main(*sys.argv)