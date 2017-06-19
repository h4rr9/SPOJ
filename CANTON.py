import math

T = input()

while T:
    N = input()

    D = int(math.ceil((math.sqrt(8*N+1)-1)/2.0))

    A = N - D*(D-1)/2
    B = D+1-A

    if D&1:
        print 'TERM {0} IS {1}/{2}'.format(N,B,A)
    else:
        print 'TERM {0} IS {1}/{2}'.format(N,A,B)

    T-=1
