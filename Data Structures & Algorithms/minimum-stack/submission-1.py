class MinStack:

    def __init__(self):
        self.stack_list = []
        self.minstack_list = []
        

    def push(self, val: int) -> None:
        self.stack_list.append(val)
        if not self.minstack_list:
            self.minstack_list.append(val) # when min stack is empty
        else:
            if val <= self.minstack_list[-1]:
                self.minstack_list.append(val)

    def pop(self) -> None:
        if self.stack_list[-1] == self.minstack_list[-1]:
            self.minstack_list.pop()
        self.stack_list.pop()
        

    def top(self) -> int:
        return self.stack_list[-1]
        

    def getMin(self) -> int:
        return self.minstack_list[-1]
