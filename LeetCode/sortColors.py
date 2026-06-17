class Solution:
    def sortColors(self, nums):
        zero = 0
        one = 0
        two = 0

        for num in nums:
            if num == 0:
                zero += 1
            elif num == 1:
                one += 1
            else:
                two += 1

        index = 0

        for _ in range(zero):
            nums[index] = 0
            index += 1

        for _ in range(one):
            nums[index] = 1
            index += 1

        for _ in range(two):
            nums[index] = 2
            index += 1