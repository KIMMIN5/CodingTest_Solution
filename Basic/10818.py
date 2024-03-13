def solution():
    max = 0 
    min = 0
    A = []
    N = int(input())
    A = list(map(int, input().split()))

    for i in range(len(A)):
        if i == 0:
            max = A[i]
        if max < A[i]:
            max = A[i]    
        
    

    for j in range(len(A)):
        if(j == 0):
            min = A[j]
        if min > A[j]:
            min = A[j]   
    print("{} {}".format(min, max))         
    

solution()