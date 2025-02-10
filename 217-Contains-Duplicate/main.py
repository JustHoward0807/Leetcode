class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Ideas:
        # 1. Sort list and two pointers to check duplicate
        # 2. Hashmap, if not exist, put in there and if exist just return false

        # dict = {}
        # for num in nums:
        #     if num in dict:
        #         return True
        #     else:
        #         dict[num] = num

        # return False 

        # sorted_list = sorted(nums)
        # for index in range(len(sorted_list)):
        #     if (index != len(sorted_list) - 1 and sorted_list[index] == sorted_list[index+1]):
        #         return True
        
        # return False

        # Awesome way that I found in Solutions
        if (len(nums) == len(set(nums))):
            return False
        else:
            return True
