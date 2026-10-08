class Solution:
    def isValid(self, s: str) -> bool:
        # we know that valid parentheses are like anagrams
        # loop through string and append to array if [ or { or (
        # remove from array in stack LIFO order if ] or } or )
        stack = []
        closeToOpen = {'}': '{', ']': '[', ')': '('} 
        # the hashmap is optional it just makes the comparison easier
        # we could do if conditions mapping each character with one another
        # it's not openToClose because of how we're trying to remove starting
        # parenthesis from the stack not the other way around

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0

# O(n) time complexity and space complexity