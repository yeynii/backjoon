n = int(input())
solutions = list(map(int, input().split()))
solutions.sort(reverse=True)
count = 0

for i in range(len(solutions)-1):
  if solutions[i] * 0.9 <= solutions[-1]:
    count += len(solutions) -1 -i
    continue
  
  start = i + 1
  end = len(solutions) - 1
  
  while start <= end:
    mid = (start + end) // 2
    if solutions[mid] >= solutions[i] * 0.9: # 중간 값이 찾고자 하는 값보다 크면
      start = mid + 1
    else: # 작으면
      end = mid - 1
  count += end - i
print(count)
