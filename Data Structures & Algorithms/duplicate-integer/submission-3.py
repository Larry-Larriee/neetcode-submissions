class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = dict()

        for num in nums:
            if num in hashmap:
                hashmap[num] += 1

                if hashmap[num] > 1:
                    return True
            else:
                hashmap[num] = 1
        return False