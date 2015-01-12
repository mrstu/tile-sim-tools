#!/bin/awk -f

BEGIN{nactive=0}
{
    if(NR==1) tcol=$2; 
    if(NR==2)trow=$2; 
    if(NR==3) xc=$2; 
    if(NR==4) yc=$2; 
    if(NR==6) null=$2; 
    ntot=tcol*trow; 
    if(NR>6){
        r=NR-6;
        for(i=1;i<=tcol;i++){
            if($i==null){nactive++;}
        }
    }
}
END{
    if(nactive==ntot){
        print 1
        #print 0, nactive, ntot
    }
    else{
        print 0
        #print 1, nactive, ntot};
    }
}
# This prints out a lat lon list for the center of a group of cells from an arc info dem file

#awk 'BEGIN{nactive=0}{if(NR==1) tcol=$2; if(NR==2)trow=$2; if(NR==3) xc=$2; if(NR==4) yc=$2; if(NR==6) null=$2; ntot=tcol*trow; if(NR>6) {r=NR-6; for(i=1;i<=tcol;i++){if($i==null){nactive++;}}}}END{if(nactive==ntot){print 0, nactive, ntot}else{print 1, nactive, ntot};}' "$1"
