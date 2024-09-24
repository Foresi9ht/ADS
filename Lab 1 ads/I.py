from collections import deque

def classroom_leader(n, votes):
    s_queue = deque([i for i in range(n) if votes[i] == 'S'])
    k_queue = deque([i for i in range(n) if votes[i] == 'K'])

    while s_queue and k_queue:
        if s_queue[0] < k_queue[0]:
            k_queue.popleft()
            s_queue.append(s_queue.popleft() + n)
        else:
            s_queue.popleft()
            k_queue.append(k_queue.popleft() + n)

    if s_queue:
        print("SAKAYANAGI")
    else:
        print("KATSURAGI")

n = int(input())
votes = input()
classroom_leader(n, votes)
