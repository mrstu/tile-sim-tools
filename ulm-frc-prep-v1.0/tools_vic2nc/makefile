CC        = gcc $(MY_CFLAGS)
#CC        = gcc $(MY_CFLAGS)
HDRS       = -I$(NETCDFHOME)/include
LIBRARY      = -L$(NETCDFHOME)/lib -lnetcdf
RM          = /bin/rm -f

OBJS = vic2nc.c

all : 
	make vic2nc

default:
	make vic2nc

clean :
	$(RM) *.o core log *~ 

vic2nc: $(OBJS)
	$(CC) -g -o vic2nc $(OBJS) $(LIBRARY) $(HDRS)

