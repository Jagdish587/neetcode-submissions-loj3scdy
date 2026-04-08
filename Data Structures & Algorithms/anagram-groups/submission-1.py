from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        final_result = []

        for value in strs:
            sort_value = "".join(sorted(value))
            result[sort_value].append(value)
        
        for key, value in result.items():
            final_result.append(value)
        return final_result