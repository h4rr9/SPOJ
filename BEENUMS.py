from math import sqrt,floor

def beenum(x):
    return (3+sqrt(9+12*(x-1)))/6

while True:

    n = input()
    
    if n == -1:
        break
    else:
            ans = beenum(n)

            if floor(ans) == ans:
                print 'Y'
            else:
                print 'N'
        
        
