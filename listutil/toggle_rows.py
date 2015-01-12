#!/usr/bin/env python

''''''

import os
import sys
import glob

import numpy as np
import argparse

def main(*args):
    '''Extract select cells from VIC veg, snow bands files
    
    '''
#     print args
    
    usage = "usage: %prog [options] arg"
    parser = argparse.ArgumentParser(description='Return all records with into #num_groups of files but with 0/1/0 banding')
    parser.add_argument("-g", "--num_groups",
                      dest="ngroups", default=1, type=int, help='List of row indices (zero-based, ascending order) to extract')
    parser.add_argument("-t", "--targetfile", dest="target", default=None, help="Input file")
    parser.add_argument("-o", "--outputfileprefix", dest="fileoutprefix", default=None, help="Truncated file")    

    args = parser.parse_args()

    indexfile = open(args.target,'rb')
#     target = args.target
#     outfile = open(args.outfile,'wb')    
    
    lines=indexfile.readlines()
    linelists=[]
    for nline,line in enumerate(lines):
#         line=line.rstrip()
        lparts=line.split()
        linelists.append(' '.join(lparts[1:]))
#     print linelists
    indexfile.close()
#     print rownums

    nlines=np.arange(len(linelists))
    chunks=np.array_split(nlines,args.ngroups)
    
    for nchk, chk in enumerate(chunks):        
        outfile=args.fileoutprefix+str(nchk).zfill(2)
        chklist=list(chk)
#         print chklist
        with open(outfile,'wb') as fp:
            for nline, line in enumerate(linelists):
#                 print nline
                if nline in chklist:
#                     print line
                    outline="1 "+line+"\n"
                else:
                    outline="0 "+line+"\n"
                fp.write(outline)
        fp.close()
    

if __name__=='__main__':
#     main()
    main(*sys.argv)