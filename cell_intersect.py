#!/usr/bin/env python

''''''

import os
import sys
import glob

from datetime import datetime
from datetime import timedelta

import numpy as np

def readlist(listfile):
    print listfile
    lf = open(listfile,'r')
    lf = lf.readlines()
#    for lfline in lf[:10]:
    filelist = []
    for lfline in lf:
        lfline = lfline.strip()
        lfline = lfline.split(' ')
#        print lfline
        lfline = '_'.join(lfline)
#        print lfline
        filelist.append(lfline)
    return filelist

def main(args):
    '''Parse date arguments and return number of days including last day
    
    '''
    print args[1:]
    if len(args)>1:
        filelist = {}
        for arg in args[1:]:
            print 'Arg:', arg
            filelist[arg] = (readlist(arg))
    for key in filelist.keys():
        print len(filelist[key])
        
    mar = np.in1d(filelist[args[1]], filelist[args[2]])

    # matching indices
    print len(mar[np.where(mar==True)])
    marinds = np.where(mar==True)[0]
    f = open("sub_buffer_cell_indices.txt", "w")    
    for i in marinds:
#         print 
        f.write("%d\n"%i)
    f.close()
    
    # non-matching indices
    nmrinds = np.where(mar==False)[0]
    f = open("sub_buffer_cell_indices_missing.txt", "w")    
    for i in nmrinds:
#         print 
        f.write("%d\n"%i)
    f.close()


# #        print len(filelist)
# #        print filelist
# #        print 'First 10 files:'
# #        for filerec in filelist[:10]:
# #            print filerec
#     else:
#         filelist = ['humidex_41.21875_-116.21875']
# 
#     varmap = headers()
#     
#     for fluxfile in filelist:
#         humfile = 'humidex_1915_2011/humidex_%s'%fluxfile
#         suc = os.path.exists(humfile)
#         print humfile, suc, fluxfile
# 
#         if suc:
#             os.system('cp %s king'%humfile)
#             
# ##        print 'fluxes_1915_2011/%s'%fluxfile
# #        print 'fluxes_1915_2011/fluxes_%s'%fluxfile, 'humidex_1915_2011/humidex_%s'%fluxfile
# #        procflux('fluxes_1915_2011/fluxes_%s'%fluxfile, 'humidex_1915_2011/humidex_%s'%fluxfile, varmap)
# 
# #    inttypes = "i i i "
# #    flttypes = ' '.join([21*'f'])
# #    custtype = inttypes+flttypes
# 
# #    custtype = [np.int]*3
# #    custtype.extend([np.float]*21)
# #    print custtype
# #    f = open(fluxfile)
# #    data = np.loadtxt(f, usecols=range(0,24), dtype=np.dtype(custtype[:]))


if __name__=='__main__':
    main(sys.argv)