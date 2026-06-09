class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        insert_index = 0
        for index in range(len(nums)):
            if nums[index] != val:
                nums[insert_index] = nums[index]
                insert_index = insert_index + 1
        return insert_index