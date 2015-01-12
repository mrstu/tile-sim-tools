#!/bin/bash

awk '{if(length($0)>0){if(substr($0,0,1)!="#"){printf("%s = ",$1); for(i=2;i<NF;i++){printf("%s ",$i)}; print $NF;}else{print $0}}else{print $0}}' $1