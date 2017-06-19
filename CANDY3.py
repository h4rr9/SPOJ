import sys
T = input()

while(T):
    try:
        N = input()
        s=0
        for _ in xrange(N):
            s+=int(sys.stdin.readline().rstrip())%N
            
        if s%N == 0:
            print "YES"
        else:
            print "NO"
    except SyntaxError:
        continue
    T-=1
