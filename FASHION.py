import sys, itertools

T = int(raw_input())

while(T):

    n = int(raw_input())

    m_hot = list(int(i) for i in sys.stdin.readline().rstrip().split())
    w_hot = list(int(i) for i in sys.stdin.readline().rstrip().split())

    count = 0
    for x,y in itertools.izip(sorted(m_hot),sorted(w_hot)):
        count+=x*y

    print count

    T-=1
