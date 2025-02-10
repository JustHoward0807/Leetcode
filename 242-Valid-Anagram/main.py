class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Ideas:
        #   1. HashMap or dic
        #   2. Sort and compare

        if (len(s) != len(t)):
            return False


        # dict1, dict2 = {},{}

        # for char in s:
        #     dict1[char] = dict1.get(char, 0) + 1

        # for char in t:
        #     dict2[char] = dict2.get(char, 0) + 1

        # return dict1 == dict2

        ####################################

        # sorted_String = ''.join(sorted(s))
        # sorted_String2 = ''.join(sorted(t))

        # return sorted_String == sorted_String2

        ####################################
        # Cool way I found on the internet

        return Counter(s) == Counter(t)
