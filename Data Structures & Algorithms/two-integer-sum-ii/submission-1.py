class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lhs = 0
        rhs = len(numbers) - 1

        while lhs < rhs:
            difference = numbers[rhs] + numbers[lhs]
            if difference == target:
                return[lhs+1, rhs+1]
            if difference > target:
                rhs = rhs - 1
            else:
                lhs = lhs + 1
        