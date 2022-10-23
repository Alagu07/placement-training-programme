class BinaryTreeNode:
 def __init__(self, data):
 self.data = data
 self.leftChild = None
 self.rightChild = None
def postorder(root):
 if root is None:
 return
 postorder(root.leftChild)
 postorder(root.rightChild)
 print(root.data, end=" ,")
def insert(root, newValue):
 if root is None:
 root = BinaryTreeNode(newValue)
 return root
 if newValue < root.data:
 root.leftChild = insert(root.leftChild, newValue)
 else:
 root.rightChild = insert(root.rightChild, newValue)
 return root
root = insert(None, 50)
insert(root, 20)
insert(root, 53)
insert(root, 11)
insert(root, 22)
insert(root, 52)
insert(root, 78)
print("Postorder traversal of the binary tree is:")
postorder(root)
