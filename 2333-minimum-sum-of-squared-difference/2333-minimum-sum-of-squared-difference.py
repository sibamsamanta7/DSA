from collections import Counter
from typing import List


class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        budget = k1 + k2

        # Edge case: enough budget to zero out every diff
        if sum(diffs) <= budget:
            return 0

        # Group diffs by value, sorted by height descending
        # e.g. [9, 9, 7, 5, 5] -> [(9, 2), (7, 1), (5, 2)]
        groups = sorted(Counter(diffs).items(), reverse=True)
        groups.append((0, 0))  # sentinel: floor at height 0

        group_count = 0  # elements currently in the "top group" being pushed down

        for g in range(len(groups) - 1):
            height, count = groups[g]
            next_height = groups[g + 1][0]

            group_count += count               # merge this level's bars into the group
            gap = height - next_height
            cost_to_absorb = gap * group_count # ops to drop whole group to next_height

            if budget >= cost_to_absorb:
                # Whole group drops to next_height for free-ish; continue
                budget -= cost_to_absorb
            else:
                # Budget runs out mid-drop between `height` and `next_height`
                full_drop = budget // group_count
                extra_drop_count = budget % group_count
                new_level = height - full_drop

                # (group_count - extra_drop_count) elements at new_level
                # extra_drop_count elements at new_level - 1
                result = (
                    (group_count - extra_drop_count) * new_level ** 2
                    + extra_drop_count * (new_level - 1) ** 2
                )
                # Add squares of untouched groups below (excluding sentinel)
                for h, c in groups[g + 1:-1]:
                    result += c * h * h
                return result

        return 0