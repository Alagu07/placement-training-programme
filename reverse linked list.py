class Node:
 def __init__(self, data, next=None):
 self.data = data
 self.next = next
def printList(head):
 ptr = head
 while ptr:
 print(ptr.data, end=' —> ')
 ptr = ptr.next
 print('None') 
def reverse(head, headRef):
 if head is None:
 return headRef
 first = head 
 rest = first.next 
 if rest is None:
 headRef = first
 return headRead
 headRef = reverse(rest, headRef)
 rest.next = first
 first.next = None 
 return headRef
def reverseList(head):
 return reverse(head, head)
if __name__ == '__main__':
 head = None
 for i in reversed(range(6)):
 head = Node(i + 1, head)
 head = reverseList(head)
 printList(head)
