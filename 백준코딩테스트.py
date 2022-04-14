# 10869번 사칙연산
'''
a,b = map(int, input().split())

print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
'''
# 2884 - 알람 시계
'''
h,m = map(int, input().split())

if (m < 45):
    if(h==0):
        h=24
    print('{} {}'.format(h-1, m+15))
else:
    print('{} {}'.format(h, m-45))
'''
# 1330 - 두 수 비교하기
'''
a,b = map(int, input().split())

if(a>b):
    print(">")
elif(a<b):
    print("<")
else:
    print("==")
'''
# 8393 - 1부터 n까지 합
'''
n = int(input())

sum = 0

for i in range(1, n+1):
    sum+=i

print(sum)
'''
# 4153 - 직각 삼각형
'''
while True:
    a,b,c = map(int, input().split())

    m = max(a,b,c)
    
    if a==0 and b==0 and c==0:
        break

    if(m==a):
        if(a**2 == ((b**2)+(c**2))):
            print("right")
        else:
            print("wrong")
    elif(m==b):
        if(b**2 == ((a**2)+(c**2))):
            print("right")
        else:
            print("wrong")
    else:
        if(c**2 == ((b**2)+(a**2))):
            print("right")
        else:
            print("wrong")
'''
# 2869 - 달팽이는 올라가고 싶다
'''
a,b,v = map(int, input().split())

finish = v-a
cnt = 1

if (finish<=0):
    print(cnt)
else:
    if(finish%(a-b)):
        cnt+=1
    cnt += finish//(a-b)
    print(cnt)
'''
# 9012 - 괄호
'''
n = int(input())

for i in range(n):
    s = input()
    cnt = 0
    for i in range(len(s)):
        if(s[i] == '('):
            cnt+=1
        elif(s[i] == ')'):
            cnt-=1

        if(cnt < 0):
            print('NO')
            break
    if(cnt == 0): 
        print('YES')
    elif(cnt > 0): 
        print('NO')
'''
# 1978 - 소수 찾기
'''
n = int(input())

l = list(map(int,input().split()))
count = 0 

for i in l:
    cnt = 0
    for j in range(1, i+1):
        if i%j == 0:
            cnt+=1
    if cnt==2:
        count+=1
print(count)
'''
#1065 한수
'''
n = int(input())

if(n<100):
    print(n)
else:
    cnt = 99
    for i in range(100, n+1):
        h = i//100
        t = (i%100)//10
        o = i%10

        if((h-t) == (t-o)):
            cnt+=1
    print(cnt)
'''
# 2217 - 로프
'''
n = int(input())
l = []

for i in range(n):
    l.append(int(input()))

l.sort()
m = 0

for i in range(n):
    if(l[i]*(n-i) > m):
        m = l[i]*(n-i)
print(m)
'''   
# 22352 - 항체 인식
'''
n, m = map(int, input().split())

before = []
for i in range(n):
    before.append(list(map(int, input().split())))

for i in before:
    print(i)

after = []
for i in range(n):
    after.append(list(map(int, input().split())))
    
print()

for i in after:
    print(i)
'''
# 1520 - 내리막 길
'''
import sys
import copy

sys.setrecursionlimit(10**9)
m,n = map(int,input().split())

l = [list(map(int, input().split())) for i in range(m)]
l2 = [['a' for i in range(n)] for i in range(m)]
#       위   아래    오른쪽  왼쪽
udrl=[[-1,0], [1,0], [0,1], [0,-1]]

#cnt = 0

def find(x, y):
    global cnt
    if x == m-1 and y == n-1:
        #cnt+=1
        return 1
    if l2[x][y] != 'a':
        return l2[x][y]
    
    l2[x][y] = 0

    for i in udrl:
        findx = x+i[0]
        findy = y+i[1]

        if 0 <= findx <= m-1 and 0 <= findy <= n-1:
            if l[x][y] > l[findx][findy]:
                l2[x][y] += find(findx, findy)

    return l2[x][y]

n=find(0,0)

print(n)
'''    
# 11726 - 2 * n 타일링
'''
n = 1 -> 1
n = 2 -> 2
n = 3 -> 3
n = 4 -> 5
n = 5 -> 8
n = 6 -> 13
n = 7 -> 21
n = 8 -> 34
n = 9 -> 55

0 0 0 0 0 0 0

n = 1
1 2 2 2
2 1 2 2
2 2 1 2
2 2 2 1

n = 3
2 2 1 1 1
2 1 2 1 1
2 1 1 2 1
2 1 1 1 2
1 2 2 1 1
1 2 1 2 1
1 2 1 1 2
1 1 2 2 1
1 1 2 1 2
1 1 1 2 2

n = 5
2 1 1 1 1 1
1 2 1 1 1 1
1 1 2 1 1 1
1 1 1 2 1 1
1 1 1 1 2 1
1 1 1 1 1 2

n = 7
1 1 1 1 1 1 1 1
'''
'''
import sys
sys.setrecursionlimit(10**9)
n = int(input())

l = [1, 1]

for i in range(2,n+1):
    l.append(l[i-1]+l[i-2])

result = l[n]
print(result%10007)
'''
# 19951 - 태상이의 훈련소 생활
'''
import sys
sys.setrecursionlimit(10**9)

n,m=map(int,input().split())
h = list(map(int, input().split()))
dig = [list(map(int, input().split())) for i in range(m)]
depth = {i:0 for i in range(n+1)}

for i in dig:
    depth[i[0]-1] += i[2]
    depth[i[1]] -= i[2]

for i in depth:
    if i==0 :
        h[i] += depth[i]
        continue
    depth[i] += depth[i-1]
    
    if i < len(h):
        h[i] += depth[i]


for i in h:
    print(i, end=" ")
'''
# 22352 - 항체 인식
'''
n, m = map(int, input().split())

before = [list(map(int, input().split())) for i in range(n)]
after = [list(map(int, input().split())) for i in range(n)]
diffxy = []

#       위   아래    오른쪽  왼쪽
udrl=[[-1,0], [1,0], [0,1], [0,-1]]

def find(x, y):
    diffxy.append([x,y])
    init = before[x][y]

    for i in udrl:
        findx = x+i[0]
        findy = y+i[1]
        
        if 0 <= findx < n and 0 <= findy < m and [findx, findy] not in diffxy and before[findx][findy] == init:
            #print(findx, findy)
            find(findx, findy)

end = False
for i in range(n):
    for j in range(m):
        if before[i][j] != after[i][j]:
            find(i,j)
            end = True
            break

    if end:
        break

#print(diffxy)
for i in diffxy:
    before[i[0]][i[1]] = after[diffxy[0][0]][diffxy[0][1]]

if before == after:
    print("YES")
else:
    print("NO")
'''
# 1260 dfs와 bfs
'''
from collections import deque

def dfs(n):
    visited[n] = True
    print(n, end=' ')
    for i in graph[n]:
        if not visited[i]:
            dfs(i)

def bfs(n):
    queue = deque([n])
    visited[n] = True
    while queue:
        v=queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n,m,v = map(int, input().split())
graph = [[]for i in range(n+1)]
for i in range(m):
    a,b = map(int ,input().split())
    graph[a].append(b)
    graph[b].append(a)

print(graph)
for i in range(1, n+1):
    graph[i].sort()
print()
print(graph)

visited = [False]*(n+1)

dfs(v)

print()
visited = [False]*(n+1)
        
bfs(v)
'''
# 1753 최단경로
# 서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음에 유의한다.
# 오답 if v not in l[u]:
'''
import sys
import heapq

def find(key):

    queue = []
    heapq.heappush(queue, [0, key])
    result[key] = 0


    while queue:

        queue_distance, now_key = heapq.heappop(queue)

        if result[now_key] < queue_distance:
            continue
       
        for i in l[now_key]:
            
            distance = i[1] + queue_distance

            next_key = i[0]

            
            if result[next_key] > distance:

                result[next_key] = distance
                heapq.heappush(queue, [distance, next_key])

V, e = map(int, sys.stdin.readline().strip().split())

k = int(sys.stdin.readline().strip())

l = [[] for i in range(V+1)]

result = [30000001 for i in range(V+1)]

for i in range(e):
    u, v, w = map(int, sys.stdin.readline().strip().split())
    l[u].append([v,w])

find(k)

for i in result[1:]:
    if i == 30000001:
        print("INF")
    else:
        print(i)
'''
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

import heapq

# 정점의 개수 n, 간선의 개수 m
n, m = map(int, input().split())

# 시작 정점의 번호
k = int(input())

# 무한을 의미하는 INF
INF = int(1e9)

# 그래프 초기화
graph = [[] * (n+1) for _ in range(n+1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 간선 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    # a->b가 c비용
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0

    
    while q:
        print(q)
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)

        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]

            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘을 수행
print(graph)
dijkstra(k)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
'''

































