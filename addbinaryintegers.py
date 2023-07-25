"""
Consider the problem of adding two n-bit binary integers a and b, 
stored in two n-element arrays A[0:n-1] and B[0:n-1],
where each element is either 0 or 1, 
a = the SUMMATION of A[i]*2**i and b = the SUMMATION of B[i]*2**i.

The sum c = a + b of the two integers should be stored in binary form in an
(n+1)-element array C[0:n], where c = the SUMMATION of C[i]*2**i.

Write a procedure ADD-BINARY-INTEGERS that takes as input arrays A and B, 
along with the length n and returns array C holding the sum
"""

"""


a = A[i]*(2**i)
b = B[i]*(2**i)


...
C = []
"""
A = [0, 1, 1 , 1]
B = [0, 1, 0, 1]
n = len(A) + 1
C = [0]*n

for i in range(n-1):
    if A[i] + B[i] == 2:
        C[i+1] = 1
    elif A[i] + B[i] == 1 and C[i] == 0:
        C[i] = 1
    elif A[i] + B[i] == 1 and C[i] == 1:
        C[i+1] = 1
    else:
        C[i] = C[i] + 0 

print(C)





