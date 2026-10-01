from collections import deque

class Solution(object):
    def removeInvalidParentheses(self, s):
        def isValid(str_val):
            count = 0
            for c in str_val:
                if c == "(":
                    count += 1
                elif c == ")":
                    count -= 1
                if count < 0:
                    return False
            return count == 0

        ans = []
        visited = {s}
        queue = deque([s])
        found = False

            
          
               
