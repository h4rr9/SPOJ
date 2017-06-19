import sys

T = input()
a = []
N,C = 0,0
def min_possible(x):

    cow_placed = 1
    last_pos = a[0]

    for d in a[1:]:
        if d - last_pos >=x:
            cow_placed+=1
            if cow_placed == C:
                return 1
            last_pos = d
    return 0

def binSearch():

    start,end,mid = 0,a[N-1],None

    while start<end:
        mid = (start + end)/2

        if min_possible(mid) == 1:
            start = mid + 1
        else:
            end = mid
    return start-1            

while T:
    N,C = (int(i) for i in sys.stdin.readline().rstrip().split())
    a = []
    
    for _ in xrange(N):
        a.append(int(raw_input()))

    a.sort()

    print binSearch()

    T-=1
