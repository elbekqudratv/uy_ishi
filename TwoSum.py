class Solution:
    def twoSum(self, nums, target):
        num_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i
        return []  # Agar echim topilmagan bo'lsa bo'sh list qaytariladi

# Test qismi
solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))  # [0, 1]
print(solution.twoSum([3, 2, 4], 6))  # [1, 2]
print(solution.twoSum([3, 3], 6))  # [0, 1]
