import math

testcase = int(input())
for _ in range(testcase):
    n, r = map(int,input().split(' '))
    print(math.comb(r, n)) 