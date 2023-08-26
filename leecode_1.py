# find the two numbers that add up to make up the number, and return the location of the two numbers

# 法一
# def twosum(nums, target):
#     for i in range(len(nums)):
#         res = target - nums[i]
#         if res in nums[i + 1:]:
#             return [i, nums[i + 1:].index(res) + i + 1]

# 法二
class Solution:
    nums = input('nums =')
    target = input('target =')
    def twosum(self, nums: [int], target: int):
        a, b = -1, -1
        for x in nums:
            a += 1
            for y in nums:
                b += 1
                b = b % len(nums)
                if x + y == target and a != b:
                    return [a, b]
        return []

