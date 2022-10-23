def is_anagram(str1,str2):
 return sorted(str1)==sorted(str2)
str1='abcd'
str2='dbac'
print(is_anagram(str1,str2))
