import sys,math

while True:
    a,b = (int(i) for i in sys.stdin.readline().rstrip().split())

    if a==-1 and b==-1:
        break
    else:
        print "%.0f" % math.ceil(float(max(a,b))/(min(a,b)+1))
