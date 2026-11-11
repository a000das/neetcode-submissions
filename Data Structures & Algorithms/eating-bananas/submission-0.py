class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)  # k = max(piles) always works (one pile per hour)

        while l < r:
            mid = l + (r - l) // 2
            # ceil(p / mid) using integer math
            hours = sum((p + mid - 1) // mid for p in piles)

            if hours <= h:
                r = mid        # mid is fast enough, try slower
            else:
                l = mid + 1    # too slow, need a higher rate

        return l