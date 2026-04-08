class Solution:
    def isPalindrome(self, s: str) -> bool:
        my_new_list = [val.lower() for val in s if val.isalnum()]
        return my_new_list == my_new_list[::-1]