class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        # dict
        # instead of sorting each word to check for anagram we can
        # check if they have the same characters with a count array

        # ord converts a character to int representation (ASCII)
        for s in strs:
            count = [0] * 26 # a - z and if there is a match add 1 to that letter

            for c in s:
                count[ord(c) - ord("a")] += 1
            
            # tuples can be a key as long as the data inside is
            # immutable like a string
            d[tuple(count)].append(s) 

        return list(d.values())