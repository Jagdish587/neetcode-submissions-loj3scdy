from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_dict = defaultdict(list)
        for str in strs:
            sorted_str = ''.join(sorted(str))
            result_dict[sorted_str].append(str)
        return result_dict.values()
        