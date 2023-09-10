class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}

        for x in range(len(nums)):
            valor = target - nums[x]
            if valor in dict:
                return [dict[valor], x]
            dict[nums[x]] = x
