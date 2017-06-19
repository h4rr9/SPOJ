import sys
while True:

    A,D = (int(i) for i in sys.stdin.readline().rstrip().split())

    if A == 0 and D == 0:
        break
    A_dist = set(int(i) for i in sys.stdin.readline().rstrip().split())

    D_dist = set(int(i) for i in sys.stdin.readline().rstrip().split())

    if list(D_dist)[1] <= list(A_dist)[0]:
        print 'N'
    else:
        print 'Y'
