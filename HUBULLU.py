import sys

T = input()

while T:
    N,P = (int(i) for i in sys.stdin.readline().rstrip().split())

    if P == 0:
        print 'Airborne wins.'
    else:
        print 'Pagfloyd wins.'

    T-=1
