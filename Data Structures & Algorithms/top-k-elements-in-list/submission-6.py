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
        bucket = [[] for i in range(len(nums) + 1)]

        for num in nums:
            numHashMap[num] = 1 + numHashMap.get(num, 0)
        
        for key, val in numHashMap.items():
            bucket[val].append(key)
        
        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                res.append(num)

                if len(res) == k:
                    return res