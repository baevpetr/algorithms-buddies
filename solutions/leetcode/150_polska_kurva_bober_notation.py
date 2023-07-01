import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda x, y:  int(x / y)
        }

        stack = []
        for item in tokens:
            if item not in operations:
                stack.append(int(item))
                continue
            operand_2 = stack.pop()
            operand_1 = stack.pop()
            stack.append(operations[item](operand_1, operand_2))
        return stack.pop()
