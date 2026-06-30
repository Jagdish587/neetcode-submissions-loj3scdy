class Solution:

    def is_palindrome(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left = left + 1
            right = right - 1
        return True    

    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                return self.is_palindrome(s, left, right-1) or self.is_palindrome(s, left+1, right)
            left = left + 1
            right = right - 1
        return True