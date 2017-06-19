import sys

magic = lambda n: map(str,n)

n = int(sys.stdin.readline().rstrip())

n = magic(bin(n))[2:]

if n.count('1') <=1 and n[-1] != '1':
    print 'TAK'
else:
    print 'NIE'
