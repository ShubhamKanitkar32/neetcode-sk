class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap_ag = defaultdict(list)

        for s in strs:
            key_s = str(sorted(s))
            hashmap_ag[key_s].append(s)
        
        return list(hashmap_ag.values())

        