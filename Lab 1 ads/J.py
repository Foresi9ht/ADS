from collections import deque

def deque_operations(operations):
    dq = deque()

    for op in operations:
        if op.startswith('+'):
            dq.appendleft(int(op.split()[1]))
        elif op.startswith('-'):
            dq.append(int(op.split()[1]))
        elif op == '*':
            if dq:
                print(dq[0] + dq[-1])
                dq.popleft()
                dq.pop()
            else:
                print("error")
        elif op == '!':
            return

operations = []
while True:
    try:
        op = input().strip()
        operations.append(op)
        if op == '!':
            break
    except EOFError:
        break

deque_operations(operations)
