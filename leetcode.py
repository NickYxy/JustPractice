# 1.Two Sum
'''Given an array of integers, return indices of the two numbers such that they add up to a specific target.
   You may assume that each input would have exactly one solution,
   and you may not use the same element twice.
'''

'''Examples:
   Given nums = [2, 7, 11, 15], target = 9,
   Because num[0] + num[1] = 2 + 7 = 9,
   :return [0, 1]
'''
# class Solution(object):
#     def twoSum(self, nums, target):
#         # nums = list()
#         # for i in range(len(nums)):
#         #     for j in nums:
#         #         if nums[i] + nums[j] == self.target:
#         #             return i,j
#         # return [nums[i], nums[j]]


class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                print("return the answer")
                return [buff_dict[nums[i]], i]

            else:
                print("copy the list to dict")
                buff_dict[target - nums[i]] = i

solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 26))

# This is a O(n) complexity

2.