import sys

def acode(n):
    b = [0]*5010
    b[0] = 1

    for i in xrange(1,len(n)):
        x = n[i-1]*10 + n[i]
        
        if n[i]:
            b[i] = b[i-1]
        if x > 9 and x < 27:
            if i == 1:
                b[i] = b[i] + 1
            else:
                b[i] = b[i] + b[i-2]

    return b[len(n)-1]

magic = lambda n: map(int,n)

while True:

    n = magic(sys.stdin.readline().rstrip())

    if n[0] == 0:
        break
    else:
        print acode(n)
        
