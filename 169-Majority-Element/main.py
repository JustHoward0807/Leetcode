class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Idea:
        # Straightforward thinking about using Dict
        # dic = Counter(nums)
        # return max(dic, key=dic.get)

        nums.sort()
        return nums[len(nums) // 2]

        