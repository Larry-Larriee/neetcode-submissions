class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # given array of integers sorted we want to return the indices of two numbers
        # such that they add up to the target number and you cannot use the same index
        # twice

        # but this must be O(1) solution which means the standard storing a hashmap
        # is not going to work because the size of the hashmap would add up to O(n)

        # because it's sorted, two add up to the target using a pointer at the start
        # of the array and the one at the end of the array and add up both of them 
        # to get the target value and this would produce O(n) time complexity and O(1)
        # space complexity

        finger1 = 0
        finger2 = len(numbers) - 1
        
        while finger1 < finger2: # we don't want them to collide
            total = numbers[finger1] + numbers[finger2]

            if total < target:
                # because it's sorted if total is smaller we should increase finger1
                finger1 += 1
            elif total > target:
                finger2 -= 1
            else:
                return [finger1 + 1, finger2 + 1]