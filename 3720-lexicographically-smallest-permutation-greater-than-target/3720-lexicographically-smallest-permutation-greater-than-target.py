class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        freq = Counter(s)
        result = []

        # Match target as far as possible
        i = 0

        while i < len(s) and freq[target[i]] > 0:
            result.append(target[i])
            freq[target[i]] -= 1
            i += 1

        # Start from the last valid index
        j = min(i, len(s) - 1)

        # Try positions from right to left
        while j >= 0:

            # If this character was already matched, restore it
            if j < len(result):
                ch = result.pop()
                freq[ch] += 1

            # Find the smallest available character > target[j]
            for code in range(ord(target[j]) + 1, ord('z') + 1):
                ch = chr(code)

                if freq[ch] > 0:
                    result.append(ch)
                    freq[ch] -= 1

                    # Append remaining characters in sorted order
                    for x in range(26):
                        letter = chr(ord('a') + x)
                        result.extend([letter] * freq[letter])

                    return ''.join(result)

            j -= 1

        return ""