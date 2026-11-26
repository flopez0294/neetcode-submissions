class MinStack:

    def __init__(self):
        self.arr = []
        self.minArr = []

    def push(self, val: int) -> None:
        self.arr.append(val)
        if self.minArr and self.minArr[-1] < val:
            self.minArr.append(self.minArr[-1]) 
        else: 
            self.minArr.append(val)

    def pop(self) -> None:
        self.arr.pop()
        self.minArr.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.minArr[-1]
