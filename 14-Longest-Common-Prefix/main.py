class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        strs = sorted(strs)
        first = strs[0]
        last = strs[-1]
        
        for index in range(min(len(first), len(last))):
            if first[index] != last[index]:
                return ans
            else:
                ans += first[index]
        return ans