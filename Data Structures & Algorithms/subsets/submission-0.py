class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # the goal is to find all the possible subsets of the array. This would
        # also be like a combination problem because order does not matter

        # [1,2,3] for example for any subset i'm either including or not including
        # that number in the subset so thats 2 options per number or 2 * 2 * 2 = 8
        # which is 2^n the length of the list

        # The time complexity though would be O(n * 2^n) because as we find the new
        # subset we're also copying it every single time then appending it into result 
        
        # backtracking (part of algorithms in dsa) allows us to create a tree where
        # our options are including the number or not and we end up with unique
        # combinations for each layer
        
        res = []

        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            # include the number inside of the subset
            subset.append(nums[i])
            dfs(i + 1)

            # do not include the number in the subset
            # backtrack by cleaning up the choice
            subset.pop()
            dfs(i + 1)
        dfs(0)

        return res