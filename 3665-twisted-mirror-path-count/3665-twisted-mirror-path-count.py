mat = [[[1, 1], [1, 1]], [[0, 1], [1, 0]]]
MOD = 10**9 + 7

class Solution:
    def uniquePaths(self, A: List[List[int]]) -> int:
        n, left = len(A[0]), 0
        dp = [0] * n

        dp[0] = 1

        for row in A:
            left = 0
            for j, c in enumerate(row):
                top = dp[j]

                dp[j] = (left * mat[c][1][0] + top * mat[c][1][1]) % MOD
                left  = (left * mat[c][0][0] + top * mat[c][0][1]) % MOD

        return left