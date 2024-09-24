from collections import deque

def royal_flush(n):
    q = deque(range(1, n + 1))
    result = [0] * n
    for i in range(1, n + 1):
        for _ in range(i):
            q.append(q.popleft())
        result[i - 1] = q.popleft()
    return result

T = int(input())
for _ in range(T):
    N = int(input())
    print(*royal_flush(N))
