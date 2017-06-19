import sys

T = input()

while(T):
    string = sys.stdin.readline().rstrip()
    if string == "":
        continue

    pos_equal = string.find('=')
    pos_inkBlot = string.find('machula')
    pos_plus = string.find('+')
    a = string[:pos_plus-1]
    b = string[pos_plus+2:pos_equal-1]
    c = string[pos_equal+2:]

    if pos_inkBlot > pos_equal:
        print '{0} + {1} = {2}'.format(a,b,int(a)+int(b))
    else:
        if pos_inkBlot > pos_plus:
            print '{0} + {1} = {2}'.format(a,int(c)-int(a),c)
        else:
            print '{0} + {1} = {2}'.format(int(c)-int(b),b,c)
    T-=1
