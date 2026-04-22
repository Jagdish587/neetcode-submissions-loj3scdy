class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result_str = ""
        sorted_list = sorted(strs)
        value_A = len(sorted_list[0])
        value_B = len(sorted_list[-1])
        min_val = min(value_A, value_B)   
        for index in range(min_val):
            if sorted_list[0][index] == sorted_list[-1][index]:
                result_str = result_str + sorted_list[0][index]
            else:
                break
        
        return result_str
        