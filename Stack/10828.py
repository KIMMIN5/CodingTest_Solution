'''
백준 알고리즘 연습 
10828 스택 문제 with Python
파이썬은 리스트로 간단하게 스택을 구현할 수 있어서 코드를 작성하는데 어려움이 없었다.
하지만 파이썬으로 코딩테스트를 볼 때, 입력받을 때 시간초과 때문에 sys.stdin.readline()을 사용해야 하는 것을 몰랐다.
또한, sys.stdin.readline()으로 입력값을 받게 되면 문자열로 받아지고 끝에 개행문자가 따라오기 때문에 strip를 사용하여 앞뒤에 있는 공백, 개행문자를 제거하였다.
'''

import sys

def main():
    cnt = 0
    cmd = ''
    status = ''
    value = ''
    stack = []

    cnt = int(input())
    
    for i in range(cnt):
        cmd = sys.stdin.readline().strip()
        
        if ' ' in cmd:
            status, value = cmd.split(' ')
        else:
            status = cmd
            value = None

        if status == 'push':
            stack.append(int(value))
        
        elif status == 'pop':
            if len(stack) > 0:
                print(stack.pop())
            else:
                print(-1)
        
        elif status == 'size':
            print(len(stack))

        elif status == 'empty':
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        
        elif status == 'top':
            if len(stack) > 0:
                print(stack[-1])
            else:
                print(-1)


main()