CC=gcc
CFLAGS= -shared -Wall -g -O -fPIC
RM= rm


all: print.so

clean: 
	$(RM) print.so

print.so: print.c
	$(CC) $(CFLAGS) -o $@ $<
