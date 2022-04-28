'''
n = int(input())
L = input().split()
l = [int(i) for i in L] # [50, 23, 54, 24, 123]

s_l = sorted(l) # [23, 24, 50, 54, 123]

for m, i in enumerate(s_l):
    index = l.index(i)
    l[index] = m

for i in l:
    print(i, end = ' ')
'''
'''
import operator

n, m = input().split()
n = int(n)
m = int(m)

d = {}
for i in range(n):
    k,v = input().split()
    d[k] = int(v)

d = sorted(d.items(), key = operator.itemgetter(1), reverse=True)
print(d)

cnt = 0
for i in range(m):
    if cnt >= m:
        break
    print(d[i][0])
    cnt+=1
'''
#CodeUp사이트 3015 문제
'''
n, m = input().split()
n = int(n)
m = int(m)

d = []
for i in range(n):
    k,v = input().split()
    d.append([k,int(v)])

cnt = 0
while cnt < m:
    max = 0
    max_key = 0
    for k, v in enumerate(d):
        
        if max < d[k][1]:
            max = d[k][1]
            max_key = k
    print(d[max_key][0])
    del d[max_key]
    cnt+=1
'''
#CodeUp사이트 3004 문제
'''
n = int(input())

data = list(map(int, input().split()))  # [50, 23, 54, 24, 123]

def bin_search(data, start, end, k):
    print('data = {}, start = {}, end = {}, k = {}'.format(data, start, end, k))
    while start <= end:
        mid = (start + end) // 2
        print('mid = {}, data[mid] = {}, k = {}'.format(mid, data[mid], k))
        if data[mid] == k:
            return mid
        elif data[mid] < k:
            start = mid + 1
        else:
            end = mid - 1
        print('start = {}, end = {}'. format(start, end))

def resort(data):
    index_memo = ""
    sorted_data = sorted(data)  # [23, 24, 50, 54, 123]
    for i in data:
        index_memo += str(bin_search(sorted_data, 0, len(data)-1, i)) + " "
        print('index_memo = {}'. format(index_memo))
        print()
    return index_memo

print(resort(data))
'''
#CodeUp사이트 3004 문제
'''
n = int(input())
L = list(map(int, input().split()))

def bin_search(sort_l, start, end, a):
    while start <= end:
        mid = (start + end)//2
        if sort_l[mid] == a:
            return mid
        elif sort_l[mid] > a :
            end = mid-1
        else :
            start = mid + 1

def sort(l):
    index = ""
    s_l = sorted(l)
    for i in l:
        index += str(bin_search(s_l, 0, len(l)-1, i)) + " "
    return index
print(sort(L))
'''
#CodeUp사이트 3016 문제
'''
n = int(input())
l = [list(input().split()) for i in range(n)]
result = ""

top = l[0]
for i in l[1:]:
    if int(top[1]) < int(i[1]):
        top = i
result += top[0] + " "
start = 2
while start < 4:
    cnt = 1
    for i in l:
        if top[0] != i[0] and int(top[start]) < int(i[start]):
            cnt += 1
    result += str(cnt) + " "
    start += 1

print(result)
'''
#CodeUp사이트 3019 문제
'''
n = int(input())
l = [list(input().split()) for i in range(n)]

for k,i in enumerate(l):
    for m, j in enumerate(i):
        if j.isdigit():
            l[k][m] = int(j)

l.sort(key = lambda x: (x[1], x[2], x[3], x[0]))
for i in l:
    print(i[0])
'''
#CodeUp사이트 3108 문제
'''
n = int(input())
data = [ list(input().split())for i in range(n)]

def setdata(data):
    cnt = 0
    setdata = []
    while cnt < n:
        if data[cnt][0] == 'I':
            Idata(setdata, data[cnt])
   
        elif data[cnt][0] == 'D':
            ddata(setdata, data[cnt])

        cnt+=1
    return setdata

def Idata(data, i):
    for j in data:
        if j[1] != i[1]:
            continue
        else:
            return 0
    data.append(i)
    return data

def ddata(data, i):
    deldata = []
    for j in data:
        if j[1] == i[1]:
            deldata.append(j)

    for j in deldata:
        data.remove(j)
        
    return data

def intdata(data):
    for n,i in enumerate(data):
        for m,j in enumerate(i):
            if j.isdigit():
                data[n][m] = int(j)
    return data


intdata(data)
data = setdata(data)
data.sort(key = lambda x: x[1])
findn = list(map(int, input().split()))

for i in findn:
    print('{} {}'.format(data[i-1][1], data[i-1][2]))
'''
#CodeUp사이트 3109 문제
'''
n = int(input())
l = [input().split() for i in range(n)]

def intdata(data):
    for n,i in enumerate(data):
        for m,j in enumerate(i):
            if j.isdigit():
                data[n][m] = int(j)
    return data

def setdata(data):
    setdata = []
    cnt = 0
    while cnt < n:
        if data[cnt][0] == 'I':
            Idata(setdata, data[cnt])
        elif data[cnt][0] == 'D':
            ddata(setdata, data[cnt])
        cnt+=1
    return setdata
def Idata(data, i):
    data.insert(0,i)
    return data

def ddata(data, i):

    deldata=0
    for j in data:
        if j[1] == i[1]:
            deldata = j

            break
    if deldata:
        data.remove(deldata)

    return data

intdata(l)
data = setdata(l)
data.sort(key = lambda x: x[1])
findnum = tuple(map(int, input().split()))

for i in findnum:
    print('{} {}'.format(data[i-1][1], data[i-1][2]))
'''
#CodeUp사이트 3170 문제
'''
n,m = map(int, input().split())


l = {}

def inputdata(l,n):
    
    for i in range(n):
        data = input().split()
        if data[0] not in l:
            l[data[0]] = int(data[1])
        else:
            l[data[0]] = l[data[0]]+int(data[1])
    return l

def printdata(l,m):

    for i in range(m):
        data =input()
        if data in l:
            print(l[data])
        else:
            print(0)

inputdata(l,n)
printdata(l,m)

    
N, M = map(int, input().split())
dic = {}
for i in range(N):
    S, k = input().split()
    dic[S] = dic.get(S,0) + int(k)

for i in range(M):
    Q = input()
    print(dic.get(Q, 0))
'''
#CodeUp사이트 4012 문제
'''
n = int(input())
data = list(map(int,input().split())) # [34, 55, 60, 60, 76, 80, 87, 90, 90, 100]

d = {}

s_data = sorted(data, reverse=True) # [100, 90, 90, 87, 80, 76, 60, 60, 55, 34]

cnt = 0
for i in s_data:
    cnt+=1
    if i not in d:
        d[i] = cnt
    else:
        continue
    
for i in data:
    print('{} {}'.format(i, d[i]))
'''
#CodeUp사이트 4751 문제
'''
# 첫 번째 줄에는 대회참가 학생 수를 나타내는 N 이 주어진다
n = int(input())
#두 번째 줄부터 N 개의 줄에는 각 줄마다
# 한 학생의 소속 국가 번호, 학생 번호, 그리고 성적이 하나의 빈칸을 사이에 두고 주어진다
data = [list(map(int,input().split())) for i in range(n)]
data.sort(key = lambda x: x[2], reverse=True)

prize = data[:3]
del data[:3]

while True:
    if prize[0][0] == prize[1][0] == prize[2][0]:
        del prize[-1]
        prize.append(data[0])
        del data[0]
    else:
        break

for i in prize:
    print('{} {}'.format(i[0], i[1]))
'''
#CodeUp사이트 1901 문제
'''
n = int(input())
cnt = 0
def printf(cnt):
    if cnt == n:
        return 0
    else:
        print(cnt+1)
        printf(cnt+1)

printf(cnt)
'''
#CodeUp사이트 1902 문제
'''
def printnum(n):
    if n == 0:
        return 0
    else:
        print(n)
        printnum(n-1)

n = int(input())

printnum(n)
'''
#CodeUp사이트 1904 문제
'''
a, b = map(int, input().split())

def oprint(a, b):

    if a % 2 == 0 and b % 2 == 0 and a < b:
        print(a+1)
        oprint(a+3,b-1)
    elif a % 2 == 0 and b % 2 == 1 and a <= b:
        print(a+1)
        oprint(a+3, b)
    elif a % 2 == 1 and b % 2 == 0 and a <= b:
        print(a)
        oprint(a+2, b-1)
    elif a % 2 == 1 and b % 2 == 1 and a <= b:
        print(a)
        oprint(a+2, b)
    else:
        return 0
            

oprint(a, b)
'''
#CodeUp사이트 1905 문제
'''
import sys
sys.setrecursionlimit(10**7)

def sum(nsum):
    if nsum == n:
        return nsum
    return nsum + sum(nsum+1)
    
n = int(input())
nsum = 0
print(sum(nsum))
'''
#CodeUp사이트 1912 문제
'''
def fac(n):
    if n == 1:
        return 1
    return n*fac(n-1)

n = int(input())
print(fac(n))
'''
#CodeUp사이트 1915 문제 -> 재귀함수 및 메모라이징 기법
'''
d = {0:0 , 1:1}

def fibo(n):
    if n in d:
        return d[n]
    d[n] = fibo(n-1) + fibo(n-2)
    return d[n]
    

n = int(input())
print(fibo(n)%10009)
'''
#CodeUp사이트 1920 문제
'''

def t(n):
    if n<2:
        return n%2
    return str(t(n//2))+str(n%2)

n = int(input())
print(t(n))
'''
#CodeUp사이트 1928 문제
'''
def u(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        print(n)
        return u(n//2)
    elif n % 2 == 1:
        print(n)
        return u(3*n+1)

n = int(input())
print(u(n))
'''
#CodeUp사이트 1929 문제
'''
def u(n):
    
    if n == 1:
        return n
    elif n%2 == 0:
        print(u(n//2))
        return n
    elif n % 2 == 1:
        print(u(n*3+1))
        return n

n = int(input())
print(u(n))
'''
#CodeUp사이트 1930 문제

#SuperSum(k,n)=SuperSum(k−1,1)+SuperSum(k−1,2)+...+SuperSum(k−1,n)

'''
d = {}
def SuperSum(k, n):
    if k == 0:
        d[(k,n)] = n
        return n
    if (k,n) not in d and n > 1:
        SuperSum(k,n-1)
        SuperSum(k-1,n)
        d[(k,n)] = d[(k,n-1)] + d[(k-1,n)]

    elif (k,n) not in d and n <= 1:
        SuperSum(k-1,n)
        d[(k,n)] = d[(k-1,n)]
    return d[(k,n)]


while True:
    try:
        k, n = map(int, input().split())
        print(SuperSum(k,n))
    except:
        break


#11     12      13
#01     0102    010203
'''
#CodeUp사이트 1953 문제
'''
def triangle(cnt):
    if cnt == n:
        print('*'*cnt)
        return 1
    else:
        print('*'*cnt)
        cnt+=1
        triangle(cnt)
cnt = 1
n = int(input())

triangle(cnt)
'''
#CodeUp사이트 3702 문제
'''
d = {}

def pascal(n1, n2):
    if ((n1 == 1) or (n2 == 1)):
        d[(n1,n2)] = 1
        return 1
    elif (n1, n2) not in d:
        pascal(n1-1, n2)
        pascal(n1, n2-1)
        d[(n1, n2)] = d[(n1-1,n2)]+d[(n1,n2-1)]

    return d[(n1,n2)]

r, c = map(int, input().split())
print(pascal(r,c)%100000000)
'''
#CodeUp사이트 3704 문제
'''
  1 2 3 4 5  6  

  1 2 4 7 13 23   
'''
'''
import sys
sys.setrecursionlimit(10**9)

d = { 0 : 1, 1 : 1}
def step(n):
    if n ==2:
        return d[n-1]+d[n-2]
    elif n <= 1:
        return d[n]
        
    if n not in d and n >= 3:
        d[n] = (step(n-1) + step(n-2) + step(n-3))%1000
        return d[n]
    elif n in d:
        return d[n]
        

n = int(input())

print(step(n))
'''
#CodeUp사이트 3733 문제 12월 3 일 보류
'''
sys.setrecursionlimit(10**6)

d = {1 : [1]}

def u(n):
    global l
    if n in d:
        l = l+d[n]
        return 0
    l.append(n)
    if n > 10000000:
        return u(n//2)
    
    if n % 2 == 1:
        u(n*3+1)
    elif n % 2 == 0:
        u(n//2)

a , b= map(int,input().split())

maxkey=a
for i in range(a, b+1):
    l = []
    u(i)
    d[i] = l
    if len(l) > len(d[maxkey]):
        maxkey=i

print(maxkey, len(d[maxkey]))
'''
'''
maxkey=1
for k,v in d.items():
    if len(d[k]) > len(d[maxkey]):
        maxkey = k
print(maxkey, len(d[maxkey]))
'''
'''
import sys
import operator
sys.setrecursionlimit(10**9)

d = {1 : 1}

def u(n):
    global cnt
    dcnt += 1
    if n in d:
        cnt += d[n]
        return 1

    if n % 2 == 1:
        cnt+=1
        u(n*3+1)
    elif n % 2 == 0:
        cnt+=1
        u(n//2)
    return 0

a , b= map(int, sys.stdin.readline().split())

for i in range(a, b+1):
    cnt = 0
    u(i)
    d[i] = cnt

d1 = sorted(d.items(), key=operator.itemgetter(1), reverse=True)

print(d1[0][0],d1[0][1])
'''
'''
import sys
import operator
sys.setrecursionlimit(10**9)


a , b= map(int, sys.stdin.readline().split())

d={1 : 1}
def u(a,b):
    while a < b:
        a+=1

        cnt_now = line(a)

        d[a]=cnt_now
    return max(d,key=d.get)

def line(n):
    cnt_now=0
    while True:
        if n in d:
            cnt_now=cnt_now+d[n]
            break
        elif n%2==0:
            n=n//2
        else:
            n=3*n+1
        cnt_now+=1
        if n not in d:
            cnt = line(n)
            d[n] = cnt
    return cnt_now

m = u(a-1,b)
print(int(m), d[m])
'''


#CodeUp사이트 2623
'''
def gcf(a, b):
    aL = [ i for i in range(1, a+1) if a%i == 0]
    bL = [ j for j in range(1, b+1) if b%j == 0]

    sameL = []
    for i in aL:
        for j in bL:
            if i == j:
                sameL.append(i)
    return sameL[-1]

a, b= map(int, input().split())

print(gcf(a,b))
'''

# CodeUp사이트 2625
'''
n = int(input())

triangle = []
for a in range(1, (n+1)//2):
    for b in range(1, (n+1)//2):
        for c in range(1, (n+1)//2):
            if a < (b+c) and (a+b+c) == n:
                l = [a,b,c]
                l.sort()
                triangle.append(l)

print(len(set([tuple(i) for i in triangle])))
'''
# CodeUp사이트 2626
'''
n = int(input())

def Tri(n):
    cnt = 0
    a = 0
    half = n//2

    while a < half:
        a+=1
        for b in range(a, half+1):
            c = n-a-b
            if a<=b and b<=c and c<a+b:
                cnt += 1
    return cnt
print(Tri(n))
'''    
'''
for a in range(1, (n+1)//2):
    for b in range(a,(n+1)//2):
        for c in range(b, (n+1)//2):
            if a<=b and b<=c and c<a+b and a+b+c == n:
                print(a,b,c)
                cnt+=1
print(cnt)
'''
# CodeUp사이트 2628

# 원을 1~100가지 간격 3.6, 교차가 안될 조건 평행, 그냥 교차조건 수 사이에 ㅣ있으면 대는거아닌가?
'''
a,b = map(int, input().split())
c,d = map(int, input().split())

l = [[a,b],[c,d]]
for i in l:
    i.sort()
if (l[0][0] < l[1][0] and l[1][0] < l[0][1] and l[0][1] < l[1][1]) or (l[0][0] > l[1][0] and l[0][0] < l[1][1] and l[1][1] < l[0][1]):
    print('cross')
else:
    print('not cross')
'''
# CodeUp사이트 2631
'''
import sys

n, k = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))

cnt = 0

def cntL(start):
    global cnt
    end = start+1

    if l[start] > k:
        return 0
    elif l[start] == k:
        cnt+=1
        return 0
    else:
        sumL(start, end) 
    
    return 0
        
def sumL(start, end):
    global cnt
    if end == n:
        return 0
    L = [l[i]for i in range(start,end+1)]
    suml = sum(L)
    if suml > k:
        return 0
    elif suml == k:
        cnt+=1
        return 0
    else:
        sumL(start, end+1)
        return 0


for i in range(n):
    cntL(i)
    
print(cnt)
'''

import sys

n, k = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))

cnt = 0

def tresure(start,end):
    mid = (start + end)//2
    sumL = sum(list(l[i]for i in range(start,mid)))

def n(i): 
    print(i+1,i+2,i+3)
    return i

d = {i : n(i) for i in range(n)}
#tresure(0,n)
print(cnt)
print(d)

































