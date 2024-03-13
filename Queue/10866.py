'''
백준 알고리즘 분류 덱 10866 문제를 해결하였다.
파이썬은 collections 모듈에서 deque를 제공하기 때문에 정말 쉽게 해결할 수 있었다.
'''

import sys
from collections import deque

def main():
    dequeue = deque()

    N = int(sys.stdin.readline().strip())
    string = ''

    for i in range(N):
        string = str(sys.stdin.readline().strip())
        if ' ' in string:
            cmd, item = string.split(' ')
        else:
            cmd = string
        
        if cmd == 'push_front':
            dequeue.appendleft(item)
        
        elif cmd == 'push_back':
            dequeue.append(item)

        elif cmd == 'pop_front':
            if len(dequeue) > 0:
                print(dequeue.popleft())
            else:
                print(-1)

        elif cmd == 'pop_back':
            if len(dequeue) > 0:
                print(dequeue.pop())
            else:
                print(-1)
        
        elif cmd == 'size':
            print(len(dequeue))

        elif cmd == 'empty':
            if len(dequeue) == 0:
                print(1)
            else:
                print(0)

        elif cmd == 'front':
            if len(dequeue) == 0:
                print(-1)
            else:
                print(dequeue[0])

        elif cmd == 'back':
            if len(dequeue) == 0:
                print(-1)
            else:
                print(dequeue[len(dequeue)-1])

main()