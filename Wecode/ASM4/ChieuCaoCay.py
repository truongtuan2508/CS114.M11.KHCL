#Chieu cao cua Cay
import sys 
from collections import deque
class Node:
  def __init__(self, key):
    self.left = None
    self.right = None
    self.val = key
class bst:
  def __init__(self):
    self.root = None
  def insert(self, root, key):
    if self.root is None:
      self.root = Node(key)
    else:
      if root is None:
        root = Node(key)
      elif root.val < key:
        root.right = self.insert(root.right, key)
      elif root.val > key:
        root.left = self.insert(root.left, key)
    return root
  def maxDepth(self, root):
    if root is None:
        return 0
    else :
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

myList = deque()
while True:
  lst = [int(n) for n in sys.stdin.readline().split()]
  #lst = [int(n) for n in input().split()]
  if lst[0] == 0:
    myList.appendleft(lst[1])
  elif lst[0] == 1:
    myList.append(lst[1])
  elif lst[0] == 2:
    if lst[1] in myList:
      myList.insert(myList.index(lst[1])+1,lst[2])
    else:
      myList.appendleft(lst[2])
  elif lst[0] == 3:
    break
#print(myList)
tree = bst()
root = Node(myList[0])
for i in myList:
  tree.insert(root,i)
print(tree.maxDepth(root))