class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list_to_dict = defaultdict(int)

        for num in nums:
            list_to_dict[num] = list_to_dict[num] + 1
            if list_to_dict[num] > 1:
                return True
        return False
