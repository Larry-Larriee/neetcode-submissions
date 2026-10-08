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