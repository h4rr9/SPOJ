n = int(raw_input())


count=0
if n!=1:
    for i in xrange(1,n/2+1):
        count += max(n//i-i+1,0)
else:
    count = 1
print count
