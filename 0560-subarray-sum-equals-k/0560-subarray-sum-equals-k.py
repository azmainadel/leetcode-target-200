from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        current_sum = 0
        mapping = defaultdict(int)

        mapping[0] = 1

        for num in nums:
            current_sum += num
            count += mapping[current_sum - k]
            mapping[current_sum] += 1

        return count