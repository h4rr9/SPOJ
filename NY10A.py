import sys

def KMP(text, pattern):

    pattern = list(pattern)
 
    shifts = [1] * (len(pattern) + 1)
    shift = 1
    for pos in range(len(pattern)):
        while shift <= pos and pattern[pos] != pattern[pos-shift]:
            shift += shifts[pos-shift]
        shifts[pos+1] = shift
 
    startPos = 0
    matchLen = 0
    for c in text:
        while matchLen == len(pattern) or \
              matchLen >= 0 and pattern[matchLen] != c:
            startPos += shifts[matchLen]
            matchLen -= shifts[matchLen]
        matchLen += 1
        if matchLen == len(pattern):
            yield startPos

T = input()

while T:
    N = input()
    s = sys.stdin.readline().rstrip()

    print N, len(list(KMP(s,"TTT"))), len(list(KMP(s,"TTH"))), len(list(KMP(s,"THT"))), len(list(KMP(s,"THH"))), len(list(KMP(s,"HTT"))), len(list(KMP(s,"HTH"))), len(list(KMP(s,"HHT"))), len(list(KMP(s,"HHH")))
    


    T-=1
