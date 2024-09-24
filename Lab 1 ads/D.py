def is_balanced(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return len(stack) == 0

s = input()
if is_balanced(s):
    print("YES")
else:
    print("NO")
