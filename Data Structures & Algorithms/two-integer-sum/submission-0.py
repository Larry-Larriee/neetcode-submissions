class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        # x + y = target
        # y = target - x

        for i, y in enumerate(nums):
            x = target - y
            if x in d:
                return [d[x], i]
            d[y] = i