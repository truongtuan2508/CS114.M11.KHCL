import sys 
myList = []
while True:
  lst = [int(n) for n in sys.stdin.readline().split()]
  if lst[0] == 0:
    myList.insert(0,lst[1])
  elif lst[0] == 1:
    myList.append(lst[1])
  elif lst[0] == 2:
    if lst[1] in myList:
        myList.insert(myList.index(lst[1])+1,lst[2])
    else:
      myList.insert(0,lst[2])
  elif lst[0] == 3:
    if lst[1] in myList:
        myList.remove(lst[1])
  elif lst[0] == 4:
    while lst[1] in myList:
      myList.remove(lst[1])
  elif lst[0] == 5:
    if myList:
      myList.pop(0)
  elif lst[0] == 6:
    break
if myList is None:
  print("blank")
else:
  sys.stdout.write(' '.join(map(str, myList))+"\n")