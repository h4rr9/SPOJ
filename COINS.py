import sys
a = [-1]*(10**8)

def coins(n):
    global a
    if(n/2 + n/3 + n/4 > n ):
        if n < 10**8:
            if(a[n] == -1):
                a[n] = coins(n/2) + coins(n/3) + coins(n/4)    
            return a[n]
        else:
            return coins(n/2) + coins(n/3) + coins(n/4)
    else:
        return n

while(True):
    n = sys.stdin.readline().rstrip()
    if not n:
         break
    else:
        print coins(int(n))


        
        
