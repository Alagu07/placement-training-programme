def getMedian(A, B, n, m) :
 i = 0 
 j = 0 
 m1, m2 = -1, -1
 if((m + n) % 2 == 1) : 
 for count in range(((n + m) // 2) + 1) : 
 if(i != n and j != m) : 
 if A[i] > B[j] :
 m1 = B[j]
 j += 1
 else :
 m1 = A[i]
 i += 1 
 elif(i < n) : 
 m1 = A[i]
 i += 1
 else : 
 m1 = B[j]
 j += 1 
 return m1 
 else :
 for count in range(((n + m) // 2) + 1) : 
 m2 = m1
 if(i != n and j != m) : 
 if A[i] > B[j] :
 m1 = B[j]
 j += 1
 else :
 m1 = A[i]
 i += 1 
 elif(i < n) : 
 m1 = A[i]
 i += 1
 else : 
 m1 = B[j]
 j += 1 
 return (m1 + m2)//2
