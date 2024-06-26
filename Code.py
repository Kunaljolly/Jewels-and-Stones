class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        c = 0
        for x in stones:
            if x in jewels:
                c += 1 
        return c
