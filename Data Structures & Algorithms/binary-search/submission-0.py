class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search takes the middle number of the sorted array
        # if target is less than the middle, throw away the right and
        # the middle. if target is greater than the middle, throw away
        # the left and the middle
        # if target == the middle then return the index. 
        finger1 = 0
        finger2 = len(nums) - 1

        while finger1 <= finger2:
            middle = (finger1 + finger2) // 2
            print(middle)
            if nums[middle] < target:
                finger1 = middle + 1

            elif nums[middle] > target:
                finger2 = middle - 1

            elif nums[middle] == target:
                return middle
        return -1