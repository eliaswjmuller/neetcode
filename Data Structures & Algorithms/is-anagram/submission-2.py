class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len (t):
            return False
        s_hashed = defaultdict(int)
        t_hashed = defaultdict(int)
        for i in s:
            s_hashed[i] += 1
        for i in t: 
            t_hashed[i] += 1
        if t_hashed == s_hashed:
            return True
        return False
        