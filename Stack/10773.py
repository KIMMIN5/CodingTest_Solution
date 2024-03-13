'''
백준 알고리즘분류 스택의 10773번 문제이다.

이전에 해왔던 스택 문제에 비해 생각보다 엄청 쉽게 해결하였다.
'''

import sys

def main():
    stack = []
    answer = 0

    K = int(sys.stdin.readline())

    for i in range(K):
        number = int(sys.stdin.readline())

        if number != 0:
            stack.append(number)
        else:
            stack.pop()

    for j in stack:
        answer += j
    
    print(answer)

main()