class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.minstack or val <= self.minstack[-1]:
            self.minstack.append(val)

    def pop(self) -> None:
        if not self.stack:
            return 
        
        value = self.stack.pop()
        if value == self.minstack[-1]:
            self.minstack.pop()

    def top(self) -> int:
        if not self.stack:
            return -1
        return self.stack[-1]
        
    def getMin(self) -> int:
        if not self.minstack:
            return -1
        return self.minstack[-1]
        

        
        
