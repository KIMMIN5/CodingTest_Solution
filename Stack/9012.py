'''
백준 알고리즘 연습 
9012 스택 문제 with Python

문제는 해결했지만 아직 나는 파이썬을 제대로 활용하지 못하는 것 같다. 
코드를 조금 더 간결하게 만들 수 있을 거 같지만, 파이썬 문법 지식의 부족으로 그러지 못하였다.

파이썬을 보다 파이썬스럽게 사용하는 연습을 해야할 거 같다.
'''

import sys

def main():
    stack = []
    tc = int(sys.stdin.readline())

    for i in range(tc):
        stack = []
        string = str(sys.stdin.readline().strip())

        for ch in string:
            if len(stack) == 0:
                stack.append(ch)
            elif ch == '(' or ')':
                if ch == ')':
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        stack.append(ch)
                else:
                    stack.append(ch)
                #print('1. {}'.format(stack))
            else:
                continue

        if len(stack) == 0:
            print('YES')
        else:
            print('NO')
        
main()