class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1: return False    
        my_stack_list = []
        # insert all opening brackets 
        for val in s:
            if val == "(" or val == "[" or val == "{":
                my_stack_list.append(val)
            else:
                if val == "}":
                    if my_stack_list and my_stack_list[-1] == "{":
                        print("matched")
                        my_stack_list.pop()
                    else: 
                        return False
                elif val == "]":
                    if my_stack_list and my_stack_list[-1] == "[":
                        print("matched")
                        my_stack_list.pop()
                    else:
                        return False
                elif val == ")":
                    if my_stack_list and my_stack_list[-1] == "(":
                        print("matched")
                        my_stack_list.pop()
                    else:
                        return False

        return True if not my_stack_list else False
                    