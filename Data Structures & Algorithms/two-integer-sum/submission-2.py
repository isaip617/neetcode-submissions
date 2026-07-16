class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        return_list = []

        for i in range(len(nums)):
            number_needed = target - nums[i]
            if number_needed in nums_dict:
                return_list.append(nums_dict[number_needed])
                return_list.append(i)
                return return_list
            else:
                nums_dict[nums[i]] = i
            