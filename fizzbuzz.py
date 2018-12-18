#-*- coding: utf-8-*-
szam = int(raw_input("Adj meg egy számot 1 és 100 között: "))
for x in range(szam):
    if ((x + 1) % 3) == 0 and ((x + 1) % 5) == 0:
        print "fizzbuzz"
    elif ((x+1) % 3) == 0:
        print "fizz"
    elif ((x+1) % 5) == 0:
        print "buzz"
    if ((x+1) % 3) != 0 and ((x+1) % 5) != 0:
        print x+1