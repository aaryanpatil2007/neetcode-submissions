class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        
        heapq.heapify(stones)

        while stones:
            if len(stones) == 1:
                return -heapq.heappop(stones)
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if x == y:
                continue
            else:
                heapq.heappush(stones, min(x, y) - max(x, y))

        return 0
