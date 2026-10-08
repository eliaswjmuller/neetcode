class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hashed = defaultdict(int)
        len_s = 0
        for i in s:
            s_hashed[i] += 1
            len_s += 1
        for j in t: 
            if j not in s_hashed or s_hashed[j] == 0:
                return False
            if j in s_hashed:
                s_hashed[j] -= 1
            len_s -= 1
        if len_s == 0:
            return True
        return False
        