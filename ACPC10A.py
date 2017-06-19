import sys

while True:

    x,y,z = (int(i) for i in sys.stdin.readline().rstrip().split())

    if( x == y == z == 0):
        break
    elif( y-x==z-y):
        print "AP "+ str(z+y-x)
    else:
        print "GP "+ str(z*y/x)
