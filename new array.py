def remove_element(array_nums, val):
 i = 0
 while i < len(array_nums):
 if array_nums[i] == val: array_nums.remove(array_nums[i])
 else:
 i += 1
 return len(array_nums)
print(remove_element([1, 1, 2, 3, 4, 4, 5, 6,6,6], 4))
print(remove_element([10,10,10,10,10], 10)) 
print(remove_element([10,10,10,10,10], 20)) 
print(remove_element([], 1))
