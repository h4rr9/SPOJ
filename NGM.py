import sys

num = sys.stdin.readline().rstrip()

if num[-1] == '0':
    print 2
else:
    print 1
    print num[-1]
