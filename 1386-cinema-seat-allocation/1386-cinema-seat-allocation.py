class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):
        rows = defaultdict(set)

        for row, seat in reservedSeats:
            rows[row].add(seat)

        ans = (n - len(rows)) * 2

        for seats in rows.values():
            left = all(seat not in seats for seat in [2, 3, 4, 5])
            middle = all(seat not in seats for seat in [4, 5, 6, 7])
            right = all(seat not in seats for seat in [6, 7, 8, 9])

            if left and right:
                ans += 2
            elif left or middle or right:
                ans += 1

        return ans