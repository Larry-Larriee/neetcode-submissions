class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dictionary
        # alpha-sort
        # returning an array for each anagram. result is 2d array
        d = dict()
        res = []

        for s in strs:
            # print("".join(sorted(s)))

            if "".join(sorted(s)) in d:
                d["".join(sorted(s))].append(s)
            else:
                d["".join(sorted(s))] = [s]
        
        for key, val in d.items():
            res.append(val)
        return res
