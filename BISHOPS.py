import sys
while True:
    try:
        n = int(sys.stdin.readline().rstrip())
        if n > 1:
            print 2*(n-1)
        else:
            print 1
        
    except ValueError:
        break
