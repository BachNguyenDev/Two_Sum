from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2:
            raise Exception("Array must have at least two elements")
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                # Trả về các chỉ số đã được sắp xếp để đảm bảo tính nhất quán trong kiểm thử
                # vì thứ tự trả về không quan trọng theo đề bài.
                return sorted([num_map[complement], i])
            num_map[num] = i
        raise Exception("No two sum solution")