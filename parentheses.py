import re


def valid_parentheses(string):
    parentheses = re.sub('[^()]', '', string)
    stack = []
    brackets = {")": "("}
    for i in parentheses:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if len(stack) == 0:
                return False
            if stack[-1] == brackets[i]:
                stack.pop()
            else:
                return False
    return len(stack) == 0




