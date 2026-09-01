
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    
        edges = {}
        for u, w, t in times:
            if not u in edges.keys():
                edges[u] = []
            edges[u].append((w, t))
        
        minHeap = [(0, k)]
        visit = set()
        t = 0

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            else:
                visit.add(n1)
                t = max(t, w1)
                if n1 in edges.keys():
                    for n2, w2 in edges[n1]:
                        if n2 not in visit:
                            heapq.heappush(minHeap, (w2 + w1, n2))
        
        return t if len(visit) == n else -1


