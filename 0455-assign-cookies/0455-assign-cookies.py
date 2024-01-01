class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        i, j = 0, 0
        
        if len(s) == 0: 
            return 0
        
        g.sort()
        s.sort()
        
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i += 1
            j += 1
        
        return i
    