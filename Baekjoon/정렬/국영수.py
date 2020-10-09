N = int(input())
arr = []
for i in range(N):
  person = input().split()
  arr.append([person[0], int(person[1]),int(person[2]),int(person[3])])
  
# arr = sorted(arr, key = lambda x:x[0])  
# arr = sorted(arr, key = lambda x:x[3], reverse = True)
# arr = sorted(arr, key = lambda x:x[2])
# arr = sorted(arr, key = lambda x:x[1], reverse = True)

# 위 네줄과 같은 의미이지만, 시간과 메모리 효율이 더 떨어짐
arr.sort(key=lambda x:(-int(x[1]), int(x[2]), -int(x[3]), x[0]))


for i in arr:
  print(i[0])