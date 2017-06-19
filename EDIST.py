import sys
import itertools

def EditDistance(s,t,m,n):
    d = [[0 for i in xrange(n+1)] for j in xrange(m+1)]

    for i in xrange(m+1):
        for j in xrange(n+1):

            if i==0:
                d[i][j] = j
            elif j==0:
                d[i][j] = i
            elif s[i-1] == t[j-1]:
                d[i][j] = d[i-1][j-1]
            else:
                d[i][j] = 1 + min(d[i][j-1],d[i-1][j],d[i-1][j-1])
    

    return d[m][n]
T = input()

while T:
    s1 = raw_input()
    s2 = raw_input()

    """count = abs(len(s1) - len(s2))

    for x,y in itertools.izip(s1,s2):
        if x != y:
            count+=1
    print count"""

    print EditDistance(s1,s2,len(s1),len(s2))


    T-=1
