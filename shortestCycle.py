class Solution(object):
    def findShortestCycle(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        from collections import deque

        # lista de adjacencia
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        INF = 10**9
        ans = INF

        # roda uma BFS pra cada vertice
        for s in range(n):
            if ans == 3:  # menor ciclo possível
                return 3

            dist = [-1] * n # distancia do no s
            parent = [-1] * n
            dist[s] = 0
            fila = deque([s]) 

            while fila:
                u = fila.popleft()
                for v in adj[u]:
                    if dist[v] == -1: # nao visitado
                        dist[v] = dist[u] + 1
                        parent[v] = u
                        fila.append(v)
                    elif v != parent[u]:
                        # se o no ja foi visitado eh pq temos um ciclo
                        ans = min(ans, dist[u] + dist[v] + 1)

        return -1 if ans == INF else ans