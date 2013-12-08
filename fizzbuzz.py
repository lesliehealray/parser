#!/usr/bin/env python

# fizzbuzz
for x in xrange(1,101):
    msg = ''
    if x % 3 == 0:
        msg += "fizz"
    if x % 5 == 0:
        msg += "buzz"
    if not msg:
        msg = str(x)
    print msg

#list comprehensions
s = [n**2 for n in range(10)]
v = [2**i for i in range(13)]
m = [n for n in s if n % 2 == 0]

print s; print v; print m;

tup1 = ('physics', 'chemistry', 1997, 2000);
tup2=(1,2,3,4,5,6,7);
print tup1[0]
print tup2[1:5]


#Writing multiline commands
#When a command is split among several lines with the line continuation marker \
#the continued lines can be indented in any manner;

if __name__=="__main__":
    myParams = {"server":"mpilgrim", \
                "database":"master",\
                "uid":"sa",\
                "pwd":"secret" \
                }
(M, T, W, TH, F, S, Sn) = range(7)

print range(7)


#how to convert between tuples and lists

t=('my', 'name', 'is', 'mr', 'tuple')
print t
l=list(t)
print l

x =['my', 'name', 'is', 'mr', 'list']
print x
d = tuple(x)
print d

