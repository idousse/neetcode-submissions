class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False

        # make hashmap that counts how many numbers there are for each
        # then starting from minimum, make groups of groupsize

        hand.sort()

        nums = {}
        
        for h in hand:
            nums[h] = nums.get(h, 0) + 1

        for k in list(nums.keys()):
            c = nums[k]
            if c == 0:
                continue

            for w in range(k, k + groupSize):
                if nums.get(w,0) < c:
                    return False
                nums[w] -= c

        return True