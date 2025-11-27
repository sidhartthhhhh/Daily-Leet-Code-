class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        original_directions = set()
        
        for start, end in connections:
            graph[start].append(end)
            graph[end].append(start)
            original_directions.add((start, end))
            
        visited = set ()
        queue = deque ([0])
        roads_to_change = 0
        
        while queue:
            current_city = queue.popleft ()
            visited.add(current_city)
            
            for neighbor in graph[current_city]:
                if neighbor in visited:
                    continue
                    
                    
                if (current_city, neighbor) in original_directions:
                    roads_to_change += 1
                    
                queue.append(neighbor)
                    
        return roads_to_change
                                