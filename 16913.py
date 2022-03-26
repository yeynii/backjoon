# 부분 문자열 변환
# 두 문자열 S와 T가 주어진다. T는 알파벳 소문자로만 이루어져 있고, S는 알파벳 소문자와 물음표로만 이루어져 있다.
# S의 모든 물음표를 알파벳 소문자로 바꾸려고 한다. 이때, S의 부분 문자열로 등장하는 T의 개수를 최대로 만들어보자.
# 첫째 줄에 S, 둘째 줄에 T가 주어진다. S와 T의 길이는 100,000보다 작거나 같고, 두 길이를 곱한 값은 10,000,000보다 작거나 같다.
# S의 물음표를 알파벳 소문자로 바꿨을 때, 부분 문자열로 등장할 수 있는 T의 개수의 최댓값을 출력한다.

def makeTable(arr):
  j = 0
  table = [0] * len(arr)
  for i in range(1, len(arr)):
    while j > 0 and arr[i] != arr[j]:
      j = table[j - 1]
    if arr[i] == arr[j]:
      j += 1
      table[i] = j
  return table

S = input()
T = input()

table = makeTable(T);

sum = 0
j = 0
for i in range(len(S)):
  while j > 0 and (S[i] != T[j] and S[i] != '?'):
    j = table[j -1]
  if S[i] == T[j] or S[i] == '?':
    if j == len(T) - 1:
      S = S[:i - len(T)+1] + T + S[i+1:]
      sum += 1
      j = table[j]
    else:
      j += 1

print(sum)