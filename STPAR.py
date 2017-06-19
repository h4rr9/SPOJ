import sys

while True:
    n = input()

    if n == 0:
        break
    a = list(int(i) for i in sys.stdin.readline().rstrip().split())
    b = list([-1])
    count = 1
    while a:
        if count == a[0]:
            count+=1
            a.pop(0)
        elif count == b[-1] and b[-1]!=-1:
            b.pop()
            count+=1
        else:
            b.append(a.pop(0))

    #print b, count
    while b:
        if b[-1] != -1:
            if count != b.pop():
                print 'NO'
                break
            count+=1
        else:
            print 'YES'
            break

