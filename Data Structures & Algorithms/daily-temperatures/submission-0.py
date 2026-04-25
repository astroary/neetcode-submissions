class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for curri, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                previ = stack.pop()
                res[previ] = curri - previ
            stack.append(curri)
        return res