class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Ideas:
        #   1. Using dict to append same anagrams
        anagrams_dict = {}
        ans = []

        for str in strs:
            sorted_Str = "".join(sorted(str))
            anagrams_dict[sorted_Str] = anagrams_dict.get(sorted_Str, []) + [str]
        
        for value in anagrams_dict.values():
            ans.append(value)

        return ans