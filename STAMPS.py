import sys

T = input()
m=1
while m<=T:
    
    N,n = (int(i) for i in sys.stdin.readline().rstrip().split())

    a = list(int(i) for i in sys.stdin.readline().rstrip().split())
    print 'Scenario #{0}:'.format(m)
    if sum(a) < N:
        print 'impossible'
    else:
        a = list(reversed(sorted(a)))
        s = [a[0]]

        for x in a[1:]:
            s.append(s[-1]+x)

        for x in s:
            if x >= N:
                print s.index(x)+1
                break
    print ''

    m+=1
