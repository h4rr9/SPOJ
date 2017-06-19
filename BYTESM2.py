import sys

T = input()

def max_stones(matrix,H,W):

    for i in xrange(H-2,-1,-1):
        for j in xrange(W):
            if j == 0:
                matrix[i][j] += max(matrix[i+1][j],matrix[i+1][j+1])
            elif j == W-1:
                matrix[i][j] += max(matrix[i+1][j],matrix[i+1][j-1])
            else:
                matrix[i][j] += max(matrix[i+1][j],matrix[i+1][j+1],matrix[i+1][j-1])
    return max(matrix[0])

while T:
    H,W = (int(i) for i in sys.stdin.readline().rstrip().split())
    matrix,b = [],[]

    for i in xrange(H*W):
        
        b.append(int(raw_input()))
        if (i+1)%W == 0:
            matrix.append(b)
            b = []

    print max_stones(matrix,H,W)
    T-=1
