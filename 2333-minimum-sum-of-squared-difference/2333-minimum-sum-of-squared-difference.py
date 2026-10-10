class Solution:
    def minSumSquareDiff(
        self, nums1: List[int], nums2: List[int], k1: int, k2: int
    ) -> int:
        # Calculate absolute differences between corresponding elements
        differences = [abs(a - b) for a, b in zip(nums1, nums2)]

        # Total operations available (both k1 and k2 can be used interchangeably)
        total_operations = k1 + k2

        # If we have enough operations to reduce all differences to zero
        if sum(differences) <= total_operations:
            return 0

        max_diff = max(differences)

        # Feasible function: can we reduce all differences to at most 'target'
        # using at most 'total_operations' operations?
        def feasible(target):
            operations_needed = sum(max(diff - target, 0) for diff in differences)
            return operations_needed <= total_operations

        # Binary search to find the minimum threshold using the template
        left, right = 0, max_diff - 1
        first_true_index = max_diff  # Default if no smaller threshold is feasible

        while left <= right:
            mid = (left + right) // 2
            if feasible(mid):
                first_true_index = mid
                right = mid - 1  # Try to find smaller threshold
            else:
                left = mid + 1

        optimal_threshold = first_true_index

        # Reduce all differences to at most the optimal threshold
        for i, diff in enumerate(differences):
            operations_used = max(0, diff - optimal_threshold)
            differences[i] = min(optimal_threshold, diff)
            total_operations -= operations_used

        # Distribute remaining operations to further reduce values at the threshold
        # We can only reduce values that are currently at the threshold level
        for i, diff in enumerate(differences):
            if total_operations == 0:
                break
            if diff == optimal_threshold:
                total_operations -= 1
                differences[i] -= 1

        # Calculate and return the sum of squared differences
        return sum(diff * diff for diff in differences)
