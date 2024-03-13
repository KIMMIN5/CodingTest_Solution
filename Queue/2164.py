'''
백준 알고리즘 분류 큐 2164번 문제를 해결했다.
collections 모듈 중 deque을 사용해 추가 삭제가 빨라진 큐를 구현하였다.

이후 문제에서 요구한대로 로직을 짰다.
'''

import sys
from collections import deque

def main():
    queue = deque()

    N = int(sys.stdin.readline().strip())

    for i in range(1, N+1):
        queue.append(i)
    
    for j in range(len(queue)-1):
        queue.popleft()
        
        if len(queue) != 0:
            queue.append(queue.popleft())
        
    print(queue[0])

main()