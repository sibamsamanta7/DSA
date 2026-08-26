class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left = 0
        ones = 0
        min_len = float('inf')
        answer = ""

        for right in range(len(s)):
            if s[right] == '1':
                ones += 1

            # Too many 1's, move left
            while ones > k:
                if s[left] == '1':
                    ones -= 1
                left += 1

            # We have exactly k ones
            while ones == k:
                current = s[left:right + 1]
                length = right - left + 1

                if length < min_len:
                    min_len = length
                    answer = current
                elif length == min_len and current < answer:
                    answer = current

                # Try to make the substring shorter
                if s[left] == '1':
                    ones -= 1
                left += 1

        return answer