class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap_s = defaultdict(int)
        hashmap_t = defaultdict(int)

        for c_s in s:
            hashmap_s[c_s] += 1
        for c_t in t:
            hashmap_t[c_t] += 1
        
        return hashmap_s == hashmap_t
        
        