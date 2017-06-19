import sys

def rev(n):
    return int(''.join(list(reversed(str(n)))))

T = int(raw_input())

while T:
    a,b = ( int(i) for i in sys.stdin.readline().rstrip().split() )

    print rev(rev(a) + rev(b))

    T-=1
