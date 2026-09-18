class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        n = len(s)
        left = [n] * 26
        right = [0] * 26

        # Record the leftmost and rightmost index for each character.
        for i in range(n):
            index = ord(s[i]) - ord('a')
            left[index] = min(left[index], i)
            right[index] = i

        res = []
        r = -1

        # For each character (if it's the leftmost occurrence),
        # check if it forms a valid solution.
        for i in range(n):
            if i != left[ord(s[i]) - ord('a')]:
                continue
            new_r = right[ord(s[i]) - ord('a')]
            j = i + 1
            while (j < new_r + 1) :
                if left[ord(s[j]) - ord('a')] < i:
                    print
                    new_r = n
                    break
                new_r = max(new_r, right[ord(s[j]) - ord('a')])
                j = j + 1
            if new_r < n and (i > r or new_r < right[ord(s[r]) - ord('a')]):
                if i > r:
                    res.append(s[i:new_r + 1])
                else:
                    res[-1] = s[i:new_r + 1]
                r = new_r

        return res