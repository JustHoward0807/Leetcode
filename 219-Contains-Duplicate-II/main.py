class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Idea
        #   1. Nested for loop O(N^2) (Time Limit Exceeded)
        #   2. Sliding window

        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             check = abs(i - j)
        #             if check <= k:
        #                 return True

        # return False

        # window = set()
        # for i in range(len(nums)):
        #     if nums[i] in window:
        #         return True
        #     window.add(nums[i])
        #     if len(window) > k:
        #         window.remove(nums[i - k])

        # return False


        ###########Solution found online
        set = {}
        for i in range(len(nums)):
            if nums[i] in set and abs(i - set[nums[i]]) <= k:
                return True
            set[nums[i]] = i
        return False
