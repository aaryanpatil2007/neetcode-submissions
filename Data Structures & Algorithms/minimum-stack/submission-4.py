class MinStack:


    def __init__(self):
        self.initial = []
        self.currmin = None
        self.mins = []

    def push(self, val: int) -> None:
        self.initial.append(val)
        if self.currmin is None or val <= self.currmin:
            self.currmin = val
            self.mins.append(val)

    def pop(self) -> None:
        value = self.initial.pop()
        if len(self.mins) > 0 and value == self.mins[len(self.mins) - 1]:
            self.mins.pop()
        if self.mins:
            self.currmin = self.mins[len(self.mins) - 1]
        else:
            self.currmin = None

    def top(self) -> int:
        return self.initial[len(self.initial) - 1]

    def getMin(self) -> int:
        return self.currmin
