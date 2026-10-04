class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict(int)

        for i, y in enumerate(nums):
            x = target - y
            if d.get(x) is not None:
                return [d[x], i]
            d[y] = i