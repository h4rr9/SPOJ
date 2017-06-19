import sys
T = input()

def cards(n):
    return (3*(n-1)*(n+2)/2 - (n-3))%(10**6 + 7)


while T:
    n = input()
    print cards(n)

    T-=1
