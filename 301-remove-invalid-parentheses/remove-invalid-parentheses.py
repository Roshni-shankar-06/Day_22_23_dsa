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

        while queue:
            curr = queue.popleft()
            if isValid(curr):
                ans.append(curr)
                found = True
            
            if found:
                continue

            for i in range(len(curr)):
                if curr[i] not in "()":
                    continue
                next_str = curr[:i] + curr[i+1:]
                if next_str not in visited:
                    visited.add(next_str)
                    queue.append(next_str)
                    
        return ans