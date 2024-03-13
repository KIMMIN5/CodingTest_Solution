'''
백준 스택 알고리즘 4949번
지난번에 풀었던 괄호 찾기의 약간 심화버전이다. 문자열에서 오직 괄호와 종료조건만을 조건문을 통해 확인을 한다.
파이썬에서 문자열에서 괄호를 찾을 때 'a == b' 꼴로 작성하지 않고 내 코드와 같이 
if ch in '()[]' 를 통해 아주 간결하게 작성할 수 있다는 것을 알았다.
정말이지 아직도 파이썬답게 사용하지 못하는 거 같다.

10%에서 오답이 발생하는 원인으로 문제를 제대로 이해하지 못하였다. 종료조건은 '.'을 입력해 반복문에서 벗어나도록 해야하는데 문제를 잘못 보아 저렇게 입력해도 균형잡힌것으로 판단, 
yes를 출력시켜서 오답이 발생한것이었다.

또한 sys.stdin.readline()을 통해 문자열을 입력하므로 문자열의 끝에는 항상 개행문자가 붙어있어 종료조건문을 작성할 때 문자열의 길이가 2이고 문자열이 '.\n'일 때 종료되도록 작성하였다.
'''

import sys

def main():
    answer = ''
    
    while True:
        string = str(sys.stdin.readline())
        stack = []

        if len(string) == 2 and string == '.\n':
            break

        for ch in string:
            if ch in '()[]' and len(stack) == 0:
                stack.append(ch)
                #print('1. {}'.format(stack))

            elif ch in '()':
                if ch == '(':
                    stack.append(ch)

                elif ch == ')':
                    if stack[-1] == '(':
                        stack.pop()
                        #print('2. {}'.format(stack))
                    else:
                        stack.append(ch)
                        #print('3. {}'.format(stack))

            elif ch in '[]':
                if ch == '[':
                    stack.append(ch)

                elif ch == ']':
                    if stack[-1] == '[':
                        stack.pop()
                        #print('4. {}'.format(stack))
                    else:
                        stack.append(ch)
                        #print('5. {}'.format(stack))
            elif ch == '.':
                continue
        
        if len(stack) == 0:
            answer = 'yes' 
        else:
            answer = 'no'
        
        print(answer)

main()