class MinStack:

    def __init__(self):
        self.s = []
        self.ms = []

    def push(self, val: int) -> None:
        self.s.append(val)
        if self.ms:
            currMin = self.ms[-1]
            val = min(currMin, val)
            self.ms.append(val)
        else:
            self.ms.append(val)

    def pop(self) -> None:
        self.s.pop()
        self.ms.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.ms[-1]
