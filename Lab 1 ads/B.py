def closest_younger(ages):
    N = len(ages)
    result = [-1] * N
    stack = []

    for i in range(N):
        while stack and ages[stack[-1]] >= ages[i]:
            stack.pop()
        if stack:
            result[i] = ages[stack[-1]]
        stack.append(i)
    
    return result

N = int(input())
ages = list(map(int, input().split()))
print(*closest_younger(ages))
