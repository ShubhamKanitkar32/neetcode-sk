class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <=r:
            m = (l + r) // 2
            total_time = 0
            for pile in piles:
                pile_time = math.ceil(float(pile)/m)
                total_time += pile_time

            if total_time <= h:
                res = m
                r = m - 1
            else:
                l = m + 1

        return res

                

        