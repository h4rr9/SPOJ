def no_squares(n):
    count=0
    while n>0:
        count+=n**2
        n-=1
    return count

while True:
    n = int(raw_input())
    if n == 0:
        break
    
    print no_squares(n)

     
