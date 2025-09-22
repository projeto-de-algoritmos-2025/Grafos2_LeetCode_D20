class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        # Vou guardar aqui quais salas já visitei
        visited = set()
        
        # Pilha para a busca em profundidade, começando pela sala 0 (que sempre está aberta)
        stack = [0]
        
        # Aqui começa a aventura da busca em profundidade! 
        while stack:
            room = stack.pop()
            
            # Se ainda não visitei esta sala, vou explorá-la! 
            if room not in visited:
                visited.add(room)
                
                # Pego todas as chaves (números das salas) desta sala e adiciono na pilha para explorar depois
                for key in rooms[room]:
                    if key not in visited:
                        stack.append(key)
        
        # Agora vou verificar se consegui visitar todas as salas
        return len(visited) == len(rooms)

