from math import pi

while True:

    n = input()

    if n==0:
        break
    ans = n**2/(pi*2)
    print '%.2f' % ans
