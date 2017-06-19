import sys
from collections import defaultdict

N,M = (int(i) for i in sys.stdin.readline().rstrip().split())

if N - M != 1:
    print 'NO'
else:
    graph = defaultdict(set)
    for _ in xrange(M):
        u,v = (int(i) for i in sys.stdin.readline().rstrip().split())
        graph[u].add(v)

    visited, stack,flag = set(), [1],1
    
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
        else:
            print 'NO'
            flag = 0
            break
    if flag == 1:
        if len(visited) == N:
            print 'YES'
        else:
            print 'NO'
