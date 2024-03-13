import sys

def main():
    answer = ''
    N = int(sys.stdin.readline().strip())

    if N == 1:
        file = str(sys.stdin.readline().strip())
        print(file)
    else:
        for i in range(N):
            file = str(sys.stdin.readline().strip())
            if answer == '':    
                answer = file
            else:
                for j in range(len(file)):
                    if file[j] in answer:
                        pass
                    else:
                        answer[j] = '?'
    print(answer)       

main()