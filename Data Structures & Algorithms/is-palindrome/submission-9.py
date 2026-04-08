class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = [ch.lower() for ch in s if ch.isalnum()]
        result_str = "".join(result)
        reversed_str =  result_str[::-1]
        return result_str == reversed_str