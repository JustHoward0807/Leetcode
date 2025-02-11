class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mySet = set()
        left, maxLength = 0, 0
        for right in range(len(s)):
            # We want [while] instead of [if] is because we don't want existed window still have repeated characters such as w after moving the left inside "pwwkew", and we want left pointer point at the new position where we can start checking the longest substring.
            # If the current character is already in the set, move the left pointer
            # to the right until all duplicates of s[right] are removed from the window.
            # This ensures the window always contains unique characters.
            while s[right] in mySet:
                mySet.remove(s[left])
                left+=1
            
            mySet.add(s[right])
            maxLength = max(maxLength, right - left + 1)
        
        return maxLength
        