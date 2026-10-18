class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # given integer array nums and integer k we want to return the k most 
        # frequent elements in the array

        # one solution would be to do this with a hashmap where we loop through
        # the array and keep track of the number of times that integer is repeated
        # then return a list of the top k numbers in the hashmap. 
        
        # but we still need to sort the hashmap so we can use a bucket sort which
        # allows us to maintain overall O(n) time complexity
        
        numHashMap = {}      
        bucket = [[] for i in range(len(nums))]

        for num in nums:
            if num not in numHashMap:
                numHashMap[num] = 1
            else:
                numHashMap[num] += 1
        
        for key, val in numHashMap.items():
            bucket[val - 1].append(key) # we have to subtract 1 since it's 0-indexed
        
        res = []
        for i in range(len(nums) - 1, -1, -1):
            for num in bucket[i]:
                res.append(num)

                if len(res) == k:
                    return res