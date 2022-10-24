class Node(object):
 """
 This is a Node class.
 """
 def __init__(self, value):
 self.value = value
 self.next = None
class LinkedList(object):
 def __init__(self, head=None):
 self.head = head
 def insert_node(self, data):
 """
 :param data: Node data
 :return: None
 """
 node = Node(data)
 node.next = self.head
 self.head = node
 def display_list(self):
 current = self.head
 while current:
 print(current.value, end="->")
 current = current.next
l = LinkedList()
l.insert_node(25)
l.insert_node(35)
l.insert_node(15)
l.insert_node(32)
l.insert_node(25)
l.insert_node(80)
l.insert_node(15)
l.display_list()
