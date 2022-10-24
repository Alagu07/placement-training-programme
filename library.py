def reverse(s, left, right):
 while left <= right:
 s[left], s[right] = s[right], s[left]
 left += 1
 right -= 1
def reverseByWords(s):
 s = list(s)
 n = len(s)
 beg = 0
 for i in range(n):
 if s[i] == " ":
 reverse(s, beg, i - 1)
 beg = i + 1
 reverse(s, beg, n - 1)
 reverse(s, 0, n - 1)
 s = "".join(s)
 return s
