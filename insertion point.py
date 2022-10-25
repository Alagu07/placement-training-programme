import bisect
def index(a, x):
 i = bisect.bisect_right(a, x)
 return i 
a = [1,2,4,7]
print(index(a, 6))
print(index(a, 3))
