"""
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.
"""

from collections import deque

class Solution:
    
    def isValid(self,s:str) -> bool:
        parentheses_stack = deque()
        parentheses_dict = {"(":")", "{":"}", "[":"]"}
        for symbol in s:
            if symbol in parentheses_dict:
                parentheses_stack.append(symbol)
            else:
                if not parentheses_stack:
                    return False
                top = parentheses_stack.pop()
                if parentheses_dict[top] != symbol:
                    return False
        return not parentheses_stack

if __name__=="__main__":
    inSol = Solution()
    print(inSol.isValid("()()"))

    

