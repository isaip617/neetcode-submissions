class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}

        for i in range(len(nums)):
            key = target - nums[i]
            nums_dict[key] = i

        return_value = []

        for j in range(len(nums)):
            if nums[j] in nums_dict:
                if nums_dict[nums[j]] < j:
                    return_value.append(nums_dict[nums[j]])
                    return_value.append(j)
                elif nums_dict[nums[j]] > j:
                    return_value.append(j)
                    return_value.append(nums_dict[nums[j]])
                else:
                    continue
                break

        return return_value
            