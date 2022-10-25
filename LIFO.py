import queue
q = queue.LifoQueue() 
for x in range(4):
 q.put(str(x)) 
while not q.empty():
 print(q.get(), end=" ")
print()
