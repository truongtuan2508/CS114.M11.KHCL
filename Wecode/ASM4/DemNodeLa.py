#Dem Node La
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
  def num_leaves(self, root):
    if root is None: 
      return 0
    if root.left is None and root.right is None:
      return 1
    return self.num_leaves(root.left) + self.num_leaves(root.right)
  
tree = bst()
while True:
  n = int(stdin.readline())
  #n = int(input())
  if n == 0:
    break
  tree.insert(tree.root, n)
print(tree.num_leaves(tree.root))