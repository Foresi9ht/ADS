def process_string(s):
    stack = []
    for ch in s:
        if ch == '#':
            if stack:
                stack.pop()
        else:
            stack.append(ch)
    return ''.join(stack)

s1, s2 = input().split()
if process_string(s1) == process_string(s2):
    print("Yes")
else:
    print("No")
