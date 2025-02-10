class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Ideas
        # 1. Swap the element and return how many val are there inside

        # for index in range(len(nums)):
        #     if nums[index] == val:
        #         for index2 in range(index+ 1, len(nums)):
        #             if nums[index2] != val:
        #                 # Swap (Traditional way)
        #                 # temp = nums[index2]
        #                 # nums[index2] = nums[index]
        #                 # nums[index] = temp

        #                 # Swap (Pythonic way)
        #                 nums[index], nums[index2] = nums[index2], nums[index]
        #                 break

        # countDic = Counter(nums)
 
        # return len(nums) - countDic[val]


        #######################
        # Solution online
        index = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index+=1

        return index
