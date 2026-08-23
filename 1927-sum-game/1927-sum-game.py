class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        
        left_sum = 0
        right_sum = 0
        
        left_q = 0
        right_q = 0
        
        for i, ch in enumerate(num):
            if ch == '?':
                if i < n // 2:
                    left_q += 1
                else:
                    right_q += 1
            else:
                if i < n // 2:
                    left_sum += int(ch)
                else:
                    right_sum += int(ch)

        # If total number of '?' is odd,
        # Alice gets the advantage.
        if (left_q + right_q) % 2 == 1:
            return True

        # Check whether Bob can make the sums equal
        return left_sum - right_sum != (right_q - left_q) * 9 // 2