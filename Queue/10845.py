import sys

def main():
    queue = []
    rear = 0

    N = int(sys.stdin.readline().strip())

    for _ in range(N):
        command= str(sys.stdin.readline().strip())

        if ' ' in command:
            status, item = command.split(' ')
        else:
            status = command

        if status == 'push':
            queue.append(item)
            rear += 1
            #print('rear : {}, Queue : {}'.format(rear, queue))

        elif status == 'pop':
            if len(queue) == 0:
                print(-1)
            else:
                print(queue.pop(0))
                #print('Queue : {}'.format(queue))

        elif status == 'size':
            print(len(queue))

        elif status == 'empty':
            if len(queue) == 0:
                print(1)
            else: print(0)

        elif status == 'front':
            if len(queue) == 0:
                print(-1)
            else:
                print(queue[0])

        elif status == 'back':
            if len(queue) == 0:
                print(-1)
            else:
                print(queue[-1])

main()