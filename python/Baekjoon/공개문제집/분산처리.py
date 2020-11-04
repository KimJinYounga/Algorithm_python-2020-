import sys
T = int(sys.stdin.readline())
result=[]

def makeOneLeng(target):
    while (len(str(target)) != 1):
        target = target % 10
        # 예외 ex) 10 1
        # 항상 경계값을 고려하자!
        if target==0:
            return 10
    return target

for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    array = [makeOneLeng(a)]
    for i in range(4):
        target = array[i] * a
        target = makeOneLeng(target)
        if target not in array:
            array.append(target)
        else:
            break
    result.append(array[b % len(array)-1])

for i in result:
    print(i)