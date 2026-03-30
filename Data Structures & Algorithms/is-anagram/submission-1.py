class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = defaultdict(int)
        dict_t = defaultdict(int)

        for c_s in s:
            dict_s[c_s] += 1
        for c_t in t:
            dict_t[c_t] += 1
        
        return (dict_s == dict_t)