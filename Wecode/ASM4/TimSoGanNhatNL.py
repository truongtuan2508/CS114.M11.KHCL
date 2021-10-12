#So gan nhat
import sys
import bisect
n = int(input())
arr = [int(i) for i in input().split()]
#arr = [int(i) for i in sys.stdin.readline().split()]

while True:  
  try:
    x,y = map(int, input().split())
    #x,y = map(int, sys.stdin.readline().split())
    if y > arr[-1]:
      print(arr[-x],arr[-1])
    elif y < arr[0]:
      print(arr[0],arr[x-1])
    else:
      pos = bisect.bisect_left(arr, y, 0, len(arr))
      i = pos
      j = pos + 1
      for t in range(x):
        if i < 0:
          i = -1
          j = x
          break
        elif j == len(arr):
          i = -x-1
          j = 0
          break
        elif (y - arr[i]) <= (arr[j] - y):
          i = i - 1
        else:
          j = j + 1
      print(arr[i+1], arr[j-1])
  except:
    break