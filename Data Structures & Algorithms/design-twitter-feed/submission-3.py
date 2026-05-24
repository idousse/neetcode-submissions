import heapq
from typing import List
class Twitter:

    def __init__(self):
        self.feed = {}
        self.followers = {}
        self.following = {}
        self.timestamp = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1

        if userId not in self.feed:
            self.feed[userId] = []
        
        heapq.heappush(self.feed[userId], (-self.timestamp, tweetId))


    def getNewsFeed(self, userId):
        everyone = self.following.get(userId, set()) | {userId}  # always include self, no duplicates
        
        userfeed = []
        for f in everyone:
            for tweet in self.feed.get(f, []):
                heapq.heappush(userfeed, tweet)

        res = []
        while userfeed and len(res) < 10:
            res.append(heapq.heappop(userfeed)[1])

        return res

        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()

        if followeeId not in self.followers:
            self.followers[followeeId] = set()

        self.following[followerId].add(followeeId)
        self.followers[followeeId].add(followerId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following or followeeId not in self.followers:
            return

        self.following[followerId].discard(followeeId)
        self.followers[followeeId].discard(followerId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)