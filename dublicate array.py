a = [1,1,2,3,4,4,5,6,6,6]
dup_items = set()
uniq_items = []
for x in a:
 if x not in dup_items:
 uniq_items.append(x)
 dup_items.add(x)
print(dup_items)
