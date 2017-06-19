import sys

T = int(raw_input())

while T:
    a,b = (int(i) for i in sys.stdin.readline().rstrip().split())
    if b!=0:
    	print ((a)**(b%4+4))%10
    else:
    	print 1

    T-=1
