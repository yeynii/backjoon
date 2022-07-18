n, k = map(int, input().split())

array = list(map(int, input().split()))

indexs = []

for i in range(len(array)):
  if (array[i] == 1):
    indexs.append(i)
    
if len(indexs) < k:
  answer = -1
  
else:
  answer = min([indexs[i+k-1]-indexs[i]+1 for i in range(len(indexs) - k+1)])

print(answer)
