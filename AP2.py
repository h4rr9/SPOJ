import sys

T = input()

while T:
    X,Y,Z = (int(i) for i in sys.stdin.readline().rstrip().split())

    n = 2*Z/(X+Y)
    d = (Y-X)/(n-5)
    a = X-2*d

    print n
    for i in xrange(n):
        print a+i*d, 

    T-=1
