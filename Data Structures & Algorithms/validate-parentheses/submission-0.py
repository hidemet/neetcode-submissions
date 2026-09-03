"""
Time Complexity: O(N)
Space Complexity: O(N) nel caso peggiore
"""
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        matching = { ')' : '(', '}':'{', ']' : '['}
        stack : list[str] = []

        for i in range(len(s)):
            char = s[i]
            if char in matching:
                if stack and stack[-1] == matching[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return not stack
    


        
        