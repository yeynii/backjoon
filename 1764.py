n, m = map(int, input().split())

noHear = {}

for i in range(n):
  noHear[input()] = 1

noHearAndSee=[]

for i in range(m):
  temp = input()
  if temp in noHear:
    noHearAndSee.append(temp)

noHearAndSee.sort()

print(len(noHearAndSee))
print("\n".join(noHearAndSee))