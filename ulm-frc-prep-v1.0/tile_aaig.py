#!/usr/bin/env python

import os, sys
from osgeo import gdal

'''Source: http://gis.stackexchange.com/questions/14712/foss-method-to-split-raster-into-smaller-chunks'''

dset = gdal.Open(sys.argv[1])

width = dset.RasterXSize
height = dset.RasterYSize

print width, 'x', height

tilesize = 16 #5000

for i in range(0, width, tilesize):
    for j in range(0, height, tilesize):
        w = min(i+tilesize, width) - i
        h = min(j+tilesize, height) - j
        gdaltranString = "gdal_translate -of AAIGRID -srcwin "+str(i)+", "+str(j)+", "+str(w)+", " \
            +str(h)+" " + sys.argv[1] + " " + sys.argv[2]+ "_" + str(tilesize)+ "_"+str(i).zfill(3)+"_"+str(j).zfill(3)+".asc"
        os.system(gdaltranString)