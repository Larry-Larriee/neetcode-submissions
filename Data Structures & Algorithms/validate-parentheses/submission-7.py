class Solution:
    def isValid(self, s: str) -> bool:
        # we know that valid parentheses are like anagrams
        # loop through string and append to array if [ or { or (
        # remove from array in stack LIFO order if ] or } or )
        stack = []
        for c in s:
            if c == '[' or c == '{' or c == '(':
                stack.append(c)

            elif c == ']' and len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            elif c == '}' and len(stack) != 0 and stack[-1] == '{':
                stack.pop()
            elif c == ')' and len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                return False

        return len(stack) == 0

# O(n) time complexity and space complexity
# we could use a hashmap and count that number of times that a valid parenthesis 
# appears but that makes it difficult to figure out if the order is correct and
# also it adds overhead like hash resizing 