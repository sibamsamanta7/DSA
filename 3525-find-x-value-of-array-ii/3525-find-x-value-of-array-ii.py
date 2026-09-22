from typing import List

class Solution:
  def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
    n = len(nums)

    # prod[node] stores the product of the whole segment modulo k.
    # cnt[r][node] stores the number of prefixes with remainder r.
    prod = [1] * (4 * n)
    cnt = [[0] * (4 * n) for _ in range(5)]

    # Merge the two children into their parent.
    # Right prefixes are multiplied by the full product of the left segment.
    def pull(node):
      left = node * 2
      right = left + 1

      prod[node] = (prod[left] * prod[right]) % k

      for r in range(k): cnt[r][node] = cnt[r][left]

      for r in range(k):
        nr = (prod[left] * r) % k
        cnt[nr][node] += cnt[r][right]

    # Build the segment tree.
    # A leaf has exactly one non-empty prefix: the element itself.
    def build(node, l, r):
      if l == r:
        rem = nums[l] % k

        prod[node] = rem
        cnt[rem][node] = 1

        return

      mid = (l + r) // 2

      build(node * 2, l, mid)
      build(node * 2 + 1, mid + 1, r)

      pull(node)

    # Permanently update nums[index] and rebuild the affected tree nodes.
    def update(node, l, r, index, value):
      if l == r:
        for rem in range(k): cnt[rem][node] = 0

        rem = value % k

        prod[node] = rem
        cnt[rem][node] = 1

        return

      mid = (l + r) // 2

      if index <= mid: update(node * 2, l, mid, index, value)
      else: update(node * 2 + 1, mid + 1, r, index, value)

      pull(node)

    # Merge two query results in their original left-to-right order.
    def merge(left, right):
      left_prod, left_cnt = left
      right_prod, right_cnt = right

      counts = left_cnt[:]

      for r in range(k):
        nr = (left_prod * r) % k
        counts[nr] += right_cnt[r]

      return (left_prod * right_prod) % k, counts

    # Return the combined information for range [ql, qr].
    # For each query this range is [start, n - 1].
    def query(node, l, r, ql, qr):
      if ql <= l and r <= qr: return prod[node], [cnt[x][node] for x in range(k)]

      mid = (l + r) // 2

      if qr <= mid: return query(node * 2, l, mid, ql, qr)

      if ql > mid: return query(node * 2 + 1, mid + 1, r, ql, qr)

      left = query(node * 2, l, mid, ql, qr)
      right = query(node * 2 + 1, mid + 1, r, ql, qr)

      return merge(left, right)

    # Build the tree for the initial array.
    build(1, 0, n - 1)

    result = []

    # Apply each permanent update, then analyze nums[start..n - 1].
    for index, value, start, x in queries:
      update(1, 0, n - 1, index, value)

      # counts[x] is the number of prefixes of nums[start..n - 1]
      # whose product modulo k equals x.
      _, counts = query(1, 0, n - 1, start, n - 1)
      result.append(counts[x])

    return result