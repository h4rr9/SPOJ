import sys

T = int(raw_input())

while T:

    x,y = ( int(i) for i in sys.stdin.readline().rstrip().split() )

    if x>=0 and y>=0:
        if x-y == 0:
            if x%2==0:
                print 2*x
            else:
                print 2*x-1
        elif x-y == 2:
            if x%2==0:
                print x+y
            else:
                print 2*x-3
        else:
            print 'No Number'
    else:
        print 'No Number'
    T-=1
