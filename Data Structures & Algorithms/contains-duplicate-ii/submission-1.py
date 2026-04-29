class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mydict = {}
        
        for index, num in enumerate(nums):
            if num in mydict.keys():
                diff_val = abs(mydict[num] - index)
                if diff_val <= k:
                    return True
            mydict[num] = index
        return False