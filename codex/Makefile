#________________________________________
#
#

#________________________________________
#
#

CFLAGS				= -g
LDFLAGS				= -lz
OBJS				= \
  *.class \
  *.dSYM \
  *.o
SCALAC				= scalac

#________________________________________
#
#

#
#
#

all: codewheel phase1 phase2

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

phase2: PhaseTwo.class

PhaseTwo.class: phase2.scala
	$(SCALAC) $<

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

