import sys

T = input()

while T:
    try:
        a,b = (int(i) for i in sys.stdin.readline().rstrip().split())
        c = list(int(i) for i in sys.stdin.readline().rstrip().split())
        d = list(int(i) for i in sys.stdin.readline().rstrip().split())

        if max(c) < max(d):
            print 'MechaGodzilla'
        else:
            print 'Godzilla'
        


        T-=1
    except ValueError:
        pass
