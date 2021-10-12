#Tan Suat
q = int(input())
for i in range(q):
  n, k = map(int, input().split())
  arr = [int(n) for n in input().split()]
  print(arr.count(k))