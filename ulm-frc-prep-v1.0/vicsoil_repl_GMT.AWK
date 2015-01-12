#!/usr/bin/awk -f

{
    lon=$4
    gmt=lon*24/360
    #print gmt
    $40=gmt
    #print $0
    for(i=1; i<=52; i++){
        printf("%s\t",$i)
    }
    printf("%s\n",$53)
}