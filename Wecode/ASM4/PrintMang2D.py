#print 2d Array
import sys 
r,c = map(int, input().split())
matrix = []
for i in range(r):
  #lst = [int(j) for j in sys.stdin.readline().split()]
  lst = [int(j) for j in input().split()]
  matrix.append(lst)

arr = [0]*c
for j in range(c):
  for i in range(r):
    arr[j] = max(len(str(matrix[i][j])),arr[j])

for i in range(r):
  for j in range(c):
    a = str(matrix[i][j])
    if len(a) == arr[j]:
      sys.stdout.write(a + " ")
    else:
      space = " "*(arr[j] - len(a))
      sys.stdout.write(space + a + " ")
  print()