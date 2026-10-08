class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rem_idx_dict = {}
        for i, val in enumerate(nums):
            rem = target - val
            if rem in rem_idx_dict:
                return [rem_idx_dict[rem], i]
            else: 
                rem_idx_dict[val] = i

        