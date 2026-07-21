class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = len(nums) * [0]
        postfix = len(nums) * [0]
        output = len(nums) * [0]
        for i in range(len(nums)):
            if i == 0:
                prefix[i] = 1
            else:
                prefix[i] = nums[i - 1] * prefix[i - 1]

        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                postfix[i] = 1
            else:
                postfix[i] = nums[i + 1] * postfix[i + 1]

        for i in range(len(nums)):
            output[i] = postfix[i] * prefix[i]
        print(prefix)
        print(postfix)
        return output