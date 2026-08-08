class Twitter:

    def __init__(self):

        self.following = {}
        self.tweetIDs = {}
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if not userId in self.tweetIDs.keys():
            self.tweetIDs[userId] = []
        self.tweetIDs[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.following:
            self.following[userId] = set()
        result = []
        minHeap = []
        followees = list(self.following[userId])
        if userId not in self.following[userId]:
            followees.append(userId)
        for followee in followees:
            if followee in self.tweetIDs.keys():
                index = len(self.tweetIDs[followee]) - 1
                count, tweetid = self.tweetIDs[followee][index]
                minHeap.append([count, tweetid, followee, index])
        heapq.heapify(minHeap)
        while minHeap and len(result) < 10:
            thislist = heapq.heappop(minHeap)
            count, tweetid, followee, index = thislist[0], thislist[1], thislist[2], thislist[3] - 1
            result.append(tweetid)
            if index >= 0:
                count, tweetid = self.tweetIDs[followee][index]
                heapq.heappush(minHeap, [count, tweetid, followee, index])
        return result


    def follow(self, followerId: int, followeeId: int) -> None:
        if not followerId in self.following.keys():
            self.following[followerId] = set()
        self.following[followerId].add(followeeId)

            

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following.keys():
            self.following[followerId].discard(followeeId)