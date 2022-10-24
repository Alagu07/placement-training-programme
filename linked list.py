class Node:
 def __init__(self, data):
 self.data = data
 self.next = None
class LinkedList:
 def __init__(self):
 self.head = None
 self.last_node = None
 def append(self, data):
 if self.last_node is None:
 self.head = Node(data)
 self.last_node = self.head
 else:
 self.last_node.next = Node(data)
 self.last_node = self.last_node.next
def length_llist(llist):
 length = 0
 current = llist.head
 while current:
 current = current.next
 length = length + 1
 return length
def return_n_from_last(llist, n):
 l = length_llist(llist)
 current = llist.head
 for i in range(l - 3):
 current = current.next
 return current.data
a_llist = LinkedList()
data_list = input('Please enter the elements in the linked list: ').split()
for data in data_list:
 a_llist.append(int(data))
n = int(input('The nth element from the end will be printed. Please enter 3: '))
value = return_n_from_last(a_llist, 3)
print('The nth element from the end: {}'.format(value))
