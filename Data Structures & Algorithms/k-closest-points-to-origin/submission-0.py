import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        returnlist = []
        for i in range(len(points)):
            currdist = math.sqrt((points[i][0])**2 + (points[i][1])**2)
            heapq.heappush(heap, (currdist, points[i]))
        
        for i in range(k):
            returnlist.append(heapq.heappop(heap)[1])
        
        return returnlist

