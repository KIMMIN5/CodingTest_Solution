def Count():
    number = []
    i = 0
    count = 0
    N = int(input())

    number = list(map(int, input().split()))

    v = int(input())
    
    for i in number:
        if v == i:
            count += 1
    print(count)

Count()    
