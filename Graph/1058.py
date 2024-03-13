from collections import deque
import sys

n = int(input())
friends = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    tmp = list(input().rstrip())
    for j in range(n):
        if tmp[j] == 'Y':
            friends[i][j] = 1

def bfs(n, start):
    visited = [False] * n
    queue = deque([(start, 0)])
    count = -1  

    while queue:
        current, depth = queue.popleft()

        if depth > 2:
            continue

        for friend in range(n):
            if not visited[friend] and friends[current][friend]:
                visited[friend] = True
                queue.append((friend, depth + 1))
                if depth < 2:
                    count += 1

    return count


answer = 0
for i in range(n):
    answer = max(answer, bfs(n, i))
print(answer)

