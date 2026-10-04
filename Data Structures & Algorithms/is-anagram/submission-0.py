class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)

        for s_1 in s:
            s_dict[s_1] = s_dict[s_1] + 1
        for t_1 in t:
            t_dict[t_1] = t_dict[t_1] + 1
        
        if s_dict == t_dict:
            return True
        return False