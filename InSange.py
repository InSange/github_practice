'''
def wjfeotrkqt(n):
    if(n<0):
        return n*-1
    else:
        return n

print(wjfeotrkqt(10))
print(wjfeotrkqt(-10))
print(wjfeotrkqt(0))
'''

#1부터 n까지의 합 구하기
'''
def sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

print(sum(10))
print(sum(100))

def sum_n(n):
    return n*(n+1)//2

print(sum_n(10))
print(sum_n(100))
'''

#1부터 n까지의 연속한 숫자의 제곱의 합
'''
def sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i*i
    return sum
print(sum(10))

def s(n):
    return n*(n+1)*(2*n+1)//6

print(s(100))
'''

#주어진 숫자 n개 중 가장 큰 숫자를 찾는 알고리즘
'''
def m(n):
    m = 0
    for i in range(1,len(n)):
        if(n[m] < n[i]):
            m = i
    return n[m]

list1 = [17,92,18,33,58,7,33,42,100]
print(m(list1))

def ms(n):
    m = 0
    for i in range(1,len(n)):
        if(n[m] < n[i]):
            m = i
    return m

list1 = [17,92,18,33,58,7,33,42,100]
print(ms(list1))

def min(n):
    m = 0
    for i in range(1,len(n)):
        if(n[m] > n[i]):
            m = i
    return n[m]

list1 = [17,92,18,33,58,7,33,42,100]
print(min(list1))
'''
'''
#동명이인 찾기

def same(l):
    #same = []
    s = set()
    for i in range(0, len(l)-1):
        for j in range(i+1, len(l)):
            if(l[i] == l[j]):
                #same.append(l[i]);
                #break
                s.add(l[i])
                
    return s;

people = ["Tom", "Jerry", "Mike", "Tom","Tom","Tom"]


print(same(people))
'''

#n명 중 두명을 뽑아 짝을 지을때 나올 수 있는 모든 조합
'''
def print_pairs(l):
    for i in range(len(l)-1):
        for j in range(i+1, len(l)):
            print("({} , {})".format(l[i], l[j]))
        

name = ["Tom", "Jerry", "Mike"]
print_pairs(name)
print()
name2 = ["Tom", "Jerry", "Mike", "John"]
print_pairs(name2)
'''

#팩토리얼
'''
def fac(n):
    gop = 1
    for i in range(1, n+1):
        gop*=i
    return gop

print(fac(1))
print(fac(3))
print(fac(5))
print(fac(10))
'''
'''
def fac(n):
    if n <= 1:
        return 1
    return n*fac(n-1)

print(fac(5))
'''

#1부터 n까지의 합 구하기를 재귀 호출로 구현
'''
def sum(n):
    if n==1:
        return 1
    return n+sum(n-1)

print(sum(5))
print(sum(10))
print(sum(100))
'''
#숫자 n개 중에서 최댓값 찾기를 재귀 호출로 만들어 보세요.
'''
def m(l):
    if len(l) == 1:
        return l[0]
    if l[0] < l[1]:
        del l[0]
        return m(l)
    else :
        del l[1]
        return m(l)
    
        

l = [5,1,3,4,15,6,9,72]
print(m(l))
v = [17, 92, 18, 33, 58, 7, 33, 42]
print(m(v))
'''

#최대공약수 구하기 유클리드 알고리즘
'''
def my(a, b):
    if (a%b==0) :
        return b
    else:
        return my(b, a%b)

print(my(24,60))
print(my(48,48))
'''
'''
def my(a, b):
    if (b==0) :
        return a
    else:
        return my(b, a%b)

print(my(24, 60))
'''

#피보나치 수열
'''
def fibo(n):
    if n ==0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

print(fibo(2))
print(fibo(7))
print(fibo(10))
'''
#하노이 탑
'''
def hanoi(n,l1,l3,l2):
    if n== 1:
        print(l1, "->", l3)
        return
    hanoi(n-1,l1, l2, l3)
    print(l1,"->",l3)
    hanoi(n-1, l2, l3, l1)

print("n=1")
hanoi(1,1,3,2)
print("n=2")
hanoi(2,1,3,2)
print("n=3")
hanoi(3,1,3,2)
'''
#순차 탐색
'''
def search(a, x):
    for i in range(len(a)):
        if(x == a[i]):
            return i
    return -1

l = [17,92,18,33,58,5,33,42]

print(search(l,18))
print(search(l,33))
print(search(l,900))
'''
#리스트에서 특정 숫자의 위치를 전부 찾기
'''
def search(a, x):
    result = []
    for i in range(len(a)):
        if(x == a[i]):
            result.append(i)
    return result

l = [17,92,18,33,58,5,33,42]

print(search(l,18))
print(search(l,33))
print(search(l,900))
'''
#학생번호와 이름이 리스트로 주어졌을때 학생 번호 입력시 해당 번호 학생이름을 호출
'''
def search(a, b,x):
    for i in range(len(a)):
        if x == a[i]:
            return b[i]
    return "?"

no = [39,14,67,105]
name = ["Justin","John","Mike","Summer"]
print(search(no, name, 105))
print(search(no,name,777))
'''
#선택 정렬
'''
def min(l):
    m = 0
    for i in range(len(l)):
        if l[m] > l[i]:
            m = i
    return m

def select(l):
    result = []

    while l:
        result.append(l[min(l)])
        l.pop(min(l))


    return result

a = [2,4,5,1,3]
print(select(a))
'''
#일반적인 선택정렬 알고리즘 오름차순
'''
def select(l):
    for i in range(len(l)-1):
        min = i
        for j in range(i+1, len(l)):
            if l[min] > l[j]:
                min = j
                
        l[min], l[i] = l[i], l[min]
        print(l)

a = [2,4,5,1,3]
select(a)
print(a)
'''
#일반적인 선택정렬 알고리즘 내림차순
'''
def select(l):
    for i in range(len(l)-1):
        min = i
        for j in range(i+1, len(l)):
            if l[min] < l[j]:
                min = j
                
        l[min], l[i] = l[i], l[min]
        print(l)

a = [2,4,5,1,3]
select(a)
print(a)
'''

#2019 12 7 삽입정렬
'''
def ins_sort(a):
    n = len(a)
    for i in range(1,n):
        key = a[i]
        j = i-1
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j-=1
        a[j+1] = key
        print(a)

d = [2,4,5,1,3]
ins_sort(d)
print(d)
'''
#퀵 정렬
'''
def quick_sort(a):
    n = len(a)

    if n <= 1:
        return a

    pivot = a[-1]
    g1 = []
    g2 = []

    for i in range(0, n-1):
        if a[i] <pivot:
            g1.append(a[i])
        else:
            g2.append(a[i])

    return quick_sort(g1) + [pivot]+quick_sort(g2) 
'''

#쉽게 설명한 선택정렬
'''
def 선택정렬(a):
    result = []
    while a:
        m = 0
        for i in range(1,len(a)):
            if a[m] > a[i]:
                m = i

        p = a.pop(m)
        result.append(p)

    return result

d = [2,4,5,1,3]

print(선택정렬(d))
'''
#일반적인 선택정렬
'''
def 선택정렬(a):

    for i in range(len(a)-1):
        m = i
        for j in range(i+1, len(a)):
            if a[m] > a[j]:
                m = j

        a[i], a[m] = a[m], a[i]
        print(a)


d = [2,4,5,1,3]

선택정렬(d)
print(d)
'''
'''
#일반적인 삽입정렬

def ins_sort(a):
    n = len(a)
    for i in range(1,n):
        key = a[i]
        j = i-1
        while j >= 0 and a[j] < key:
            a[j+1] = a[j]
            j-=1
            print("중간확인 : {} ".format(a))
        a[j+1] = key
        print(a)

d = [2,4,5,1,3]
ins_sort(d)
print(d)
'''
#쉬운 병합정렬
'''
def 병합정렬(a):
    if len(a) <= 1:
        return a
    mid = len(a)//2

    #a1 = a[:mid]
    #a2= a[mid:]

    #a1.sort()
    #a2.sort()

    a1 = 병합정렬(a[:mid])
    a2 = 병합정렬(a[mid:])
    
    result = []
    while a1 and a2:
        if a1[0] > a2[0]:
            result.append(a2.pop(0))
        else:
            result.append(a1.pop(0))

    while a1:
        result.append(a1.pop(0))
    while a2:
        result.append(a2.pop(0))
    return result

d = [6,8,3,9,10,1,2,4,7,5]

print(병합정렬(d))
'''
#일반적인 병합정렬
'''
def 병합정렬(a):
    if len(a) <=1 :
        return
    mid = len(a)//2

    g1 = a[:mid]
    g2 = a[mid:]

    병합정렬(g1)
    병합정렬(g2)
    g1e = 0
    g2e = 0
    ga = 0

    while g1e < len(g1) and g2e < len(g2):
        if g1[g1e] < g2[g2e]:
            a[ga] = g1[g1e]

            g1e += 1
            ga+= 1
        else:
            a[ga] = g2[g2e]
            g2e += 1
            ga += 1

    while g1e < len(g1):
        a[ga] = g1[g1e]
        g1e += 1
        ga += 1

    while g2e < len(g2):
        a[ga] = g2[g2e]
        g2e += 1
        ga += 1

d = [6,8,3,9,10,1,2,4,7,5]

병합정렬(d)
print(d)
'''
#버블정렬
'''
def bubble_sort(a):
    n = len(a)
    while True:
        changed = False

        for i in range(0, n-1):
            if a[i] > a[i+1]:
                print(a)
                a[i], a[i+1] = a[i+1], a[i]
                changed = True

        if changed == False:
            return

d = [2,4,5,1,3]
bubble_sort(d)
print(d)
'''
#삽입정렬
'''
def 삽입위치(r, v):
    for i in range(len(r)):
        if v < r[i]:
            return i
    return len(r)

def 삽입정렬(a):
    result = []
    while a:
        value = a.pop(0)
        ins_idx = 삽입위치(result, value)
        result.insert(ins_idx,value)

    return result

d = [2,4,5,1,3]
print(삽입정렬(d))
'''

#일반적인 삽입정렬
'''
def 삽입정렬(a):
    for i in range(1,len(a)):
        key = a[i]
        j = i-1

        while j>=0 and a[j] >key:
            a[j+1] = a[j]
            j -= 1
            print(a)
        a[j+1] = key

d = [2,4,5,1,3]
삽입정렬(d)
print(d)
'''

#병합정렬
'''
def 병합정렬(a):
    if len(a) <= 1:
        return a

    mid = len(a)//2
    d1 = 병합정렬(a[:mid])
    d2 = 병합정렬(a[mid:])

    result = []
    while d1 and d2 :
        if d1[0] > d2[0]:
            result.append(d2.pop(0))
        else :
            result.append(d1.pop(0))
    while d1:
        result.append(d1.pop(0))
    while d2:
        result.append(d2.pop(0))

    return result

d = [6,8,3,9,10,1,2,4,7,5]

print(병합정렬(d))
'''

#일반적인 병합정렬
'''
def 병합정렬(a):
    if len(a) <= 1:
        return

    mid = len(a)//2
    g1 = a[:mid]
    g2 = a[mid:]
    병합정렬(g1)
    병합정렬(g2)

    i1 = 0
    i2 = 0
    ia = 0

    while i1 < len(g1) and i2 < len(g2):
        if g1[i1] < g2[i2]:
            a[ia] = g1[i1]
            i1+=1
            ia+=1
        else:
            a[ia] = g2[i2]
            i2+=1
            ia+=1

    while i1 < len(g1):
        a[ia] = g1[i1]
        i1 += 1
        ia += 1
    while i2 < len(g2):
        a[ia] = g2[i2]
        i2 += 1
        ia += 1

d = [6,8,3,9,10,1,2,4,7,5]
병합정렬(d)
print(d)
'''
'''
def 병합정렬(a):
    if len(a) <=1:
        return
    mid = len(a)//2
    d1 = a[:mid]
    d2 = a[mid:]

    병합정렬(d1)
    병합정렬(d2)

    i1 = 0
    i2 = 0
    ia = 0

    while i1 < len(d1) and i2 < len(d2):
        if d1[i1] > d2[i2]:
            a[ia] = d2[i2]
            ia += 1
            i2 += 1
        else:
            a[ia] = d1[i1]
            ia+=1
            i1+=1

    while i1<len(d1):
        a[ia] = d1[i1]
        ia += 1
        i1 += 1

    while i2 < len(d2):
        a[ia] = d2[i2]
        ia+=1
        i2+=1

d = [6,8,3,9,10,1,2,4,7,5]

병합정렬(d)
print(d)
'''

#퀵정렬
'''
def 퀵정렬(a):
    if len(a) <= 1:
        return a
    pivot = a[-1]
    g1=[]
    g2=[]

    for i in range(0, len(a)-1):
        if a[i] < pivot:
            g1.append(a[i])
        else:
            g2.append(a[i])

    return 퀵정렬(g1) + [pivot] + 퀵정렬(g2)

d = [6,8,3,9,10,1,2,4,7,5]

print(퀵정렬(d))
'''
#일반적인 퀵정렬
'''
def 퀵정렬(a, start, end):
    if end-start <= 0:
        return

    pivot = a[end]
    i = start

    for j in range(start, end):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i+= 1
    a[i], a[end] = a[end], a[i]

    퀵정렬(a, start, i-1)
    퀵정렬(a, i+1, end)

d = [6,8,3,9,10,1,2,4,7,5]

퀵정렬(d, 0, len(d)-1)
print(d)
'''

def print_all_friends(g,start):
    qu = []
    done = set()
    qu.append((start,0))
    done.add(start)

    while qu:
        p,q = qu.pop(0)
        print(p,q)
        for x in g[p]:
            if x not in done:
                qu.append((x,q+1))
                done.add(x)

fr_info = { "Summer":["John", "Justin", "Mike"],
            'John': ['Summer', 'Justin'],
            'Justin':['John','Summer','Mike','May'],
            'Mike':['Summer','Justin'],
            'May':['Justin','Kim'],
            'Kim':['May'],
            'Tom':['Jerry'],
            'Jerry':['Tom']
            }

print_all_friends(fr_info,'Summer')
print()
print_all_friends(fr_info,'Jerry')

card = 'red', 4, '다이아몬드', True
print(card)







