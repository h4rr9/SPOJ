import sys

def hangover(n):
    i=2
    while n>0:
        n-=1.0/i
        i+=1

    return i-1

while True:

    n = float(sys.stdin.readline().rstrip())

    if n == 0.00:
        break
    else:
        print "{0} card(s)".format(hangover(n)-1)    
