#________________________________________
#
#

#________________________________________
#
#

CFLAGS				= -g
LDFLAGS				= -lz

#________________________________________
#
#

#
#
#

all: phase1

#
#
#

phase1: phase1.c
	cc $(CFLAGS) -o $@ $< $(LDFLAGS)

#
#
#

clean:
	-rm -fr phase1.dSYM

#
#
#

realclean: clean
	-rm -f phase1

