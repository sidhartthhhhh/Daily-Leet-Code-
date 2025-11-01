class Solution(object):
    def mostBooked(self, n, meetings):
        meetings.sort()
        free_rooms = list(range(n))
        heapq.heapify(free_rooms)
        used_rooms = []
        count = [0] * n

        for start, end in meetings:
            while used_rooms and used_rooms[0][0] <= start:
                _, room = heapq.heappop(used_rooms)
                heapq.heappush(free_rooms, room)

            duration = end - start

            if free_rooms:
                room = heapq.heappop(free_rooms)
                heapq.heappush(used_rooms, (end, room))
            else:
                earliest_end, room = heapq.heappop(used_rooms)
                heapq.heappush(used_rooms, (earliest_end + duration, room))

            count[room] += 1

        return min([i for i in range(n) if count[i] == max(count)])