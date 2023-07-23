# This is a reminder for how to execute recurssive programs
# Python program to display the Fibonacci sequence

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 10


# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))


# memoization
>>> cache = {0: 0, 1: 1}

>>> def fibonacci_of(n):
...     if n in cache:  # Base case
...         return cache[n]
...     # Compute and cache the Fibonacci number
...     cache[n] = fibonacci_of(n - 1) + fibonacci_of(n - 2)  # Recursive case
...     return cache[n]

>>> [fibonacci_of(n) for n in range(15)]
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]