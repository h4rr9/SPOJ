while(True):
    c = input()

    if c == 0:
        break

    string = raw_input()
    r = len(string)/c
    s = ''
    for i in xrange(r):
        if i%2==1:
            s+=string[i*c+c-1:i*c-1:-1]
        else:
            s+=string[i*c:i*c+c]
    message = ''
    for i in xrange(c):
        message+=s[i::c]
    print message
