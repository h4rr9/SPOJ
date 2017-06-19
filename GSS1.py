import sys

def maxSubarray(i,j):

    global a

    max_ending_here = max_ending_sofar = a[i]

    for x in a[i+1:j]:

        max_ending_here = max(max_ending_here,max_ending_here + x)

        max_ending_sofar = max(max_ending_sofar,max_ending_here)

    return max_ending_sofar

N = int(raw_input())

a = [ int(i) for i in sys.stdin.readline().rstrip().split()]

M = int(raw_input())

for _ in xrange(M):
    x,y = ( int(i) for i in sys.stdin.readline().rstrip().split())

    print maxSubarray(x,y)

    
