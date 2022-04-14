import sys
input = sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))
K = int(input())

def count(n):
    if n == 0:
        if a[0] < K:
            return 1
        else:
            return 0
    if a[n] < K:
        return 1 + count(n-1)
    else:
        return count(n-1)

print(count(N-1)+1)
