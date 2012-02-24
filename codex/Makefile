#________________________________________
#
#

#________________________________________
#
#

CFLAGS				= -g
LDFLAGS				= -lz
OBJS				= \
  *.dSYM \
  *.o

#________________________________________
#
#

#
#
#

all: codewheel phase1

#
#
#

codewheel: codewheel.o
	cc -o $@ $< $(LDFLAGS)

codewheel.o: codewheel.c codewheel.h
	cc $(CFLAGS) -c $< -o $@

#
#
#

phase1: phase1.c
	cc $(CFLAGS) -o $@ $< $(LDFLAGS)

#
#
#

clean:
	-rm -fr $(OBJS)

#
#
#

realclean: clean
	-rm -f phase1

