class Solution(object):
    def maxNumEdgesToRemove(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        
        # Estrutura Union-Find para gerenciar componentes conectados.
        
        class UnionFind:
            __slots__ = ['parent', 'rank', 'components']
            
            def __init__(self, size):
                # Cada nó começa como seu próprio pai 
                self.parent = list(range(size))
                
                self.rank = [0] * size
                
                self.components = size - 1
            
            def find(self, x):
                
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]
            
            def union(self, x, y):
                # Encontra as raízes dos conjuntos de x e y.
                root_x = self.find(x)
                root_y = self.find(y)
                
                # Se já estão no mesmo conjunto, não precisa unir (seria ciclo).
                if root_x == root_y:
                    return False
                
                # União por rank: anexamos a árvore menor à maior,
                
                if self.rank[root_x] < self.rank[root_y]:
                    self.parent[root_x] = root_y
                elif self.rank[root_x] > self.rank[root_y]:
                    self.parent[root_y] = root_x
                else:
                    
                    self.parent[root_y] = root_x
                    self.rank[root_x] += 1
                

                self.components -= 1
                return True
            
            def is_connected(self):
               
                return self.components == 1
        
        
        alice_uf = UnionFind(n + 1)
        bob_uf = UnionFind(n + 1)
        
     
        edges_used = 0
        
      
        for edge_type, u, v in edges:
            if edge_type == 3:
                # Tentamos unir nos dois grafos.
                alice_used = alice_uf.union(u, v)
                bob_used = bob_uf.union(u, v)
                
                # Se pelo menos um aproveitou, a aresta é válida.
                if alice_used or bob_used:
                    edges_used += 1
                    
                # Se os dois grafos já estão conectados, podemos encerrar cedo.
                if alice_uf.is_connected() and bob_uf.is_connected():
                    return len(edges) - edges_used
        
        
        # Isso é parecido com o restante do Kruskal, só que separado.
        for edge_type, u, v in edges:
            if edge_type == 1:
                # Aresta exclusiva de Alice.
                if alice_uf.union(u, v):
                    edges_used += 1
                    if alice_uf.is_connected() and bob_uf.is_connected():
                        return len(edges) - edges_used
            elif edge_type == 2:
                # Aresta exclusiva do Bob.
                if bob_uf.union(u, v):
                    edges_used += 1
                    if alice_uf.is_connected() and bob_uf.is_connected():
                        return len(edges) - edges_used
        
        # No final, só é possível se os dois grafos ficaram conectados.
        # Caso contrário, retornamos -1 (não tem como).
        return len(edges) - edges_used if alice_uf.is_connected() and bob_uf.is_connected() else -1
