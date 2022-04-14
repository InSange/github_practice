"""
n = int(input("정수를 입력하십시오. "))

num = 1

for i in range(n):
    for j in range(n):
        print((num)%10, end = " ")
        num+=2
    print()
"""



def minus(a):
    minu = 0
    for i in range(1,len(a)):
        if a[minu] > a[i]:
            minu = i
    return minu

def sort(a):
    result = []
    while a:
        minu = minus(a)
        value = a.pop(minu)
        result.append(value)
    return result

list1 = [16, 25, 49,17,5,26]
print(sort(list1))

