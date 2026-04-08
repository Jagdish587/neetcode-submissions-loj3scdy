class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        my_list = []
        operators_list = ["+", "-", "*", "/"]

        for value in tokens:
            if value in operators_list:
                print("value = ", value)
                value_2 =  int(my_list.pop())
                value_1 = int(my_list.pop())
                if value == "+":
                    result = value_1 + value_2
                elif value == "-":
                    result = value_1 - value_2
                elif value == "*":
                    result = value_1 * value_2
                elif value == "/":
                    result = value_1 / value_2
                my_list.append(result)
            else:
                my_list.append(value)

        return int(my_list[0])
        