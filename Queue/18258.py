'''
백준 18258번 큐2 구현
List로 구현 시 pop(0)의 Time Complexity가 O(n)이기 때문에, 시간초과가 발생한다.
이를 해결하기 위해 Collection module중 deque를 이용하여 구현한다.
deque은 이중연결리스트 형태로 되어있어서 처음, 마지막 요소의 접근이 용이하다. 따라서 Time Complexity는 O(1)이다.

method로는 List와 동일한 append(), extend(), pop() 등 이 있고, appendleft(), extendleft(), popleft()가 추가로 있다.
'''

import sys
from collections import deque

def main():
    deq = deque()
    string = ''
    cmd = ''
    item = 0
    N = int(sys.stdin.readline().strip())

    for i in range(N):
        string = str(sys.stdin.readline().strip())

        if ' ' in string:
            cmd, item = string.split(' ')

            if cmd == 'push':
                deq.append(item)
        else:
            cmd = string
            if cmd == 'pop':
                if len(deq) != 0:
                    print(deq.popleft())
                else:
                    print(-1)
                    
            elif cmd == 'size':
                print(len(deq))
            
            elif cmd == 'empty':
                if len(deq) == 0:
                    print(1)
                else:
                    print(0)
            
            elif cmd == 'front':
                if len(deq) == 0:
                    print(-1)
                else:
                    print(deq[0])
            
            elif cmd == 'back':
                if len(deq) == 0:
                    print(-1)
                else:
                    print(deq[len(deq)-1])

main()