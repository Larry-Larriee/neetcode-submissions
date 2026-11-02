class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # goal is to find the longest substring without duplicate characters
        # one way we could possibly do this is a sliding window where the
        # window grows. To maintain O(n) we can use a set to check if the
        # window has a duplicate character and then keep shifting the first
        # pointer until the without duplicate characters is satisfied
        
        charSet = set()
        res = 0
        l = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])

            if res < len(charSet):
                res = len(charSet)
        return res
     