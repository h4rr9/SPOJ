while(True):
    n = int(raw_input())
    if n==-1:
        break
    a = list()

    for _ in xrange(n):
        a.append(int(raw_input()))

    if(sum(a)%n != 0):
        print -1
    else:
        count = 0
        for x in a:
            if x > sum(a)/n:
                count+=x-sum(a)/n
        else:
            print count
