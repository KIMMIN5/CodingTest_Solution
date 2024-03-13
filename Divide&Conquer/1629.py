'''
백준 1629번 곱셉
A, B, C 모두 최대 21억의 자연수가 입력될 수 있기 때문에, 단순히 A^B를 하게 되면 Time Complextity가 O(n)이 되기 때문에 시간초과가 발생한다.
이를 분할정복 Divide & Conquer 기법을 사용하여 복잡도를 O(logn)으로 줄여주어야 한다.
이를 위해 재귀적 호출을 통해 지수를 나눠주어 풀이를 하였다.
'''

import sys

def solution(A, B, C):
    if B == 0:
        return 1
    if B == 1:
        return A % C
    if B % 2 == 0:
        return ((solution(A, B//2, C)**2)%C)
    else:
        return (((solution(A, B//2, C)**2)*A)%C)
        

def main():
    answer = 1
    A, B, C = map(int, sys.stdin.readline().strip().split())
    answer = solution(A, B, C)
    print(answer)

main()