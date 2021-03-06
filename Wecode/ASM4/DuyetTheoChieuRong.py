#Duyet theo chieu rong
from sys import stdin
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
  def printLevelOrder(self,root):
    q = []
    q.append(root)
    while len(q) != 0:
      temp = q.pop(0)
      print(temp.val, end = ' ')
      if temp.left:
        q.append(temp.left)
      if temp.right:
        q.append(temp.right)


tree = bst()
while True:
  #n = int(stdin.readline())
  n = int(input())
  if n == 0:
    break
  tree.insert(tree.root, n)
tree.printLevelOrder(tree.root)