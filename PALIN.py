import sys
from itertools import izip

def is_palindrome(num):

    for x,y in izip(num[:len(num)/2],num[len(num):len(num)/2-1:-1]):
        if x != y:
            return False
    return True



T = input()

magic = lambda num: map(int,num)

while T:

    a = magic(sys.stdin.readline().rstrip())
    l = len(a)

    
    if(is_palindrome(a) == False):

        if l%2==0:
            i = l/2-1
            j = l/2
        else:
            i = l/2 - 1
            j = l/2 + 1
        flag = None

        while i>=0:
            if a[i] > a[j]:
                flag = 1
                break
            elif a[i] < a[j]:
                flag = 2
                break
            i-=1
            j+=1

        if l%2==0:
            i = l/2-1
            j = l/2
        else:
            i = l/2 - 1
            j = l/2 + 1

        if flag == 1:
            while i>=0:
                a[j] = a[i]
                i-=1
                j+=1
        elif flag == 2 and l&1 and a[l/2] < 9:
            a[l/2]+=1

            while i>=0:
                a[j] = a[i]
                i-=1
                j+=1
        else:
            if l&1:
                a[l/2] = 0

            while i>=0:
                if a[i] < 9:
                    a[i]+=1
                    a[j] = a[i]
                    break

                else:
                    a[j] = a[i] = 0

                i-=1
                j+=1

            while i>=0:
                a[j] = a[i]
                i-=1
                j+=1
            
    else:

        if l%2 == 0:
            i = l/2-1
            j = l/2

            while(i>=0):

                if(a[i] < 9):
                    a[i]+=1
                    a[j]+=1
                    break;
                else:
                    a[i] = a[j] = 0

                i-=1
                j+=1
            if i < 0:
                a = [1]
                a.extend([0]*(l-1))
                a.append(1)
                
        else:
            if(a[l/2] < 9):
                a[l/2]+=1
            else:
                a[l/2] = 0

                i = l/2-1
                j = l/2+1
            
                while(i>=0):

                    if(a[i]<9):
                        a[i]+=1
                        a[j]+=1
                        break
                    else:
                        a[i] = a[j] = 0
                    i-=1
                    j+=1
                if i < 0:
                    a = [1]
                    a.extend([0]*(l-1))
                    a.append(1)

    print ''.join(str(x) for x in a)
    

    T-=1
