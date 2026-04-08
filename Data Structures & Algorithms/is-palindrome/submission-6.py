class Solution:
    def isPalindrome(self, s: str) -> bool:
        my_list = list(s)
        start_index = 0
        end_index = len(my_list) - 1

        while (start_index < end_index):
            while((start_index < end_index) and not my_list[start_index].isalnum()):
                start_index +=1
            while((start_index < end_index) and not my_list[end_index].isalnum()):
                end_index -=1
            if my_list[start_index].lower() != my_list[end_index].lower():
                return False
            start_index += 1
            end_index -= 1
        return True