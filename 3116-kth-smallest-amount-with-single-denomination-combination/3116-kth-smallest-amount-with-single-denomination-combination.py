class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        # Remove redundant coins.
        # If a coin is a multiple of a smaller coin,
        # all its multiples are already covered.
        coins.sort()
        valid = []

        for coin in coins:
            if all(coin % prev != 0 for prev in valid):
                valid.append(coin)

        coins = valid
        n = len(coins)

        def lcm(a, b):
            return a // gcd(a, b) * b

        # Count numbers <= x divisible by at least one coin
        def count(x):
            total = 0

            for mask in range(1, 1 << n):
                current_lcm = 1
                bits = 0

                for i in range(n):
                    if mask & (1 << i):
                        current_lcm = lcm(current_lcm, coins[i])
                        bits += 1

                        # LCM too large, contributes nothing
                        if current_lcm > x:
                            break

                else:
                    if bits % 2 == 1:
                        total += x // current_lcm
                    else:
                        total -= x // current_lcm

            return total

        # Binary search for kth smallest amount
        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left