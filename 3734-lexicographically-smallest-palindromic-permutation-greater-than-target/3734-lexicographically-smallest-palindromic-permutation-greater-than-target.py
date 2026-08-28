class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        if n == 1: return s if s > target else ""
        cnt = [0] * 26
        for c in s: cnt[ord(c) - ord("a")] += 1
        odd_char = ""
        for i in range(26):
            if cnt[i] % 2 == 1:
                if odd_char != "": return ""
                odd_char = chr(ord("a") + i)
            cnt[i] //= 2
        prefix = []
        for i in range(n // 2):
            placed = False
            for j in range(26):
                if cnt[j] > 0:
                    cnt[j] -= 1; char_j = chr(ord('a') + j); prefix.append(char_j)
                    rem_left = []
                    for k in range(25, -1, -1): rem_left.extend([chr(ord('a') + k)] * cnt[k])
                    cand_left = "".join(prefix + rem_left)
                    cand_pal = cand_left + odd_char + cand_left[::-1]
                    if cand_pal > target:
                        placed = True; break
                    prefix.pop(); cnt[j] += 1
            if not placed: return ""
        final_left = "".join(prefix)
        return final_left + odd_char + final_left[::-1]