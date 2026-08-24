class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)

        # Convert stones into prefix sums
        for i in range(1, n):
            stones[i] += stones[i - 1]

        # dp represents the best score difference
        dp = stones[-1]

        # Work backwards
        for i in range(n - 2, 0, -1):
            dp = max(dp, stones[i] - dp)

        return dp