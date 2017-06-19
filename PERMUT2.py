import sys

while True:

    n = input()

    if(n == 0):
        break
    
    a = list(int(i)-1 for i in sys.stdin.readline().rstrip().split())

    for i in xrange(len(a)/2+1):
        if a[a[i]] != i:
            print 'not ambiguous'
            break
    else:
        print 'ambiguous'
            
        
