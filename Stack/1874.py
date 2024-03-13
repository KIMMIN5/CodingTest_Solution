'''
백준 스택 알고리즘 1874번을 해결하였다.

처음 문제를 읽은 후 이해가 되지 않아, 이해를 도와주는 영상을 시청 후 풀이를 하였다.

문제의 핵심은 오름차순으로 스택에 푸쉬를 해야하는데 스택의 top부분에 해당하는 숫자를 입력하지 않을 시 수열을 만들 수 없음을 출력해야한다.

나는 알고리즘 방식은 맞았지만 17%에서 출력초과 에러메시지가 발생하면서 난관에 막혔다. 하지만 이는 단순한 출력 방식의 문제였고 출력방식을 입력 후 한 번에 다 출력하는 방식으로 바꾸니 해결되었다.

이 문제는 단순했지만 설명이 빈약해 처음에는 어려웠다. 설명이 조금 더 친절했다면 좋을 거 같다.
'''

import sys

def manage_max(max_n, cycle):
    if max_n < cycle:
        for i in range(cycle):
            max_n += 1
            if max_n == cycle: break

    return max_n

def main():
    stack = []
    answer = ''
    max_n = 0

    n = int(sys.stdin.readline().strip())

    for i in range(n): # 8 0~7 8회 반복
        number = int(sys.stdin.readline().strip()) # 4

        if 0 < number and number <= n: # true
            if number < max_n and stack[-1] != number:
                answer = 'NO'
                break
            
            if len(stack) != 0 and stack[-1] == number:
                stack.pop()
                answer += '-\n'
            
            
            for j in range(max_n+1, number+1): # 1~4
                stack.append(j)
                #print('j = {}'.format(j))
                answer += '+\n'
                max_n = manage_max(max_n, number)
                #print('max = {}'.format(max_n))

                if stack[-1] == number:
                    stack.pop()
                    #print(stack)
                    answer += '-\n'
    
    print(answer)

main()