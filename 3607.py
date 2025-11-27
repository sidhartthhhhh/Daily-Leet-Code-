class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
            
        station_to_grid = {}  
        grid_online_stations = defaultdict(SortedList)

        grid_id_counter = 0
        visited = set()
        
        for station in range(1, c + 1):
            if station not in visited:
                grid_id_counter += 1
                q = deque([station])
                visited.add(station)
                
                while q:
                    current_station = q.popleft()
                    station_to_grid[current_station] = grid_id_counter
                    grid_online_stations[grid_id_counter].add(current_station)
                    
                    for neighbor in graph[current_station]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            q.append(neighbor)
        
        query_answers = []
        for query_type, station in queries:
            
            my_grid_id = station_to_grid.get(station, -1) 
            if my_grid_id == -1:
                if query_type == 1:
                    query_answers.append(-1)
                continue
                
            online_list = grid_online_stations[my_grid_id]
            
            if query_type == 2:
                if station in online_list:
                    online_list.remove(station)
            else:
                if station in online_list:
                    query_answers.append(station)
                else:
                    if not online_list:
                        query_answers.append(-1)
                    else:
                        query_answers.append(online_list[0]) 
                        
        return query_answers