import sys
from collections import defaultdict


N = input()
graph = defaultdict(set)

def bfs(graph,start):
    visited,queue,level=set(),[start],[0]*(N)

    while queue:
        vertex = queue.pop(0)

        if vertex not in visited:
            visited.add(vertex)

        unvisited = graph[vertex] - visited
        for i in unvisited:
            level[i-1] = 1 + level[vertex-1]
        queue.extend(unvisited)

    return max(level),level.index(max(level))+1

for _ in xrange(N-1):
    u,v = (int(i) for i in sys.stdin.readline().rstrip().split())
    graph[u].add(v)
    graph[v].add(u)

level1,node1 = bfs(graph,1)
level2,node2 = bfs(graph,node1)

print level2
