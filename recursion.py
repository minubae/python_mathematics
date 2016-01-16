# Title: Mathematical Algorithms - Recursion in Python
# Date: Oct/27/2015, Tuesday - Current
# Author: Minwoo Bae (minubae.nyc@gmail.com)
# Reference: http://wphooper.com/teaching/2015-fall-308/python/Recursion.html

import math


# 01) Factorial by Recursion
def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)

def factorial_01(n):
	if n==0 or n==1:
	   	return 1
	return factorial_01(n-1)*n
        
       
# 02) Pascal's triangle
# Consider a polynomial p(t)=aktk+ak−1tk−1+…+a1t+a0. Observe that
# (t+1)p(t)=aktk+1+(ak+ak−1)tk+(ak−1+ak−2)tk−1+…+(a0+a1)t+a0.
# We can define a sequence of polynomials by q0=1 and inductively defining qn+1(t)=(t+1)qn(t) for integers n≥0. 
# Then each qn(t) is a polynomial of degree n. We define an,k to be the coefficient of the tk term of the polynomial qn(t). 
# When arranged into a rectangular array, these numbers are known as Pascal's triangle.
# Problem: Write a recursive function pascals_triangle(n,k) which returns an,k 
# when provided an integer n≥0 and an integer k satisfying 0≤k≤n.
# To do this, first observe that the constant term of qn(t) is always one, as is the coefficient of tn in qn(t). 
# That is, qn,0=1 and qn,n=1 for all integers n≥0.
# Second, using the formula relating the coefficients for (t+1)p(t) to the coefficients for p(t) above, 
# we see that an,k=an−1,k−1+an−1,k when 0<k<n.
def pascals_triangle(n,k):
    if k==0 or k==n:
        return 1
    return pascals_triangle(n-1,k-1)+pascals_triangle(n-1,k)

# 03) Expansion of a number in base b
def expansion(n,b):
    if n<b:
        return [n]
    a0 = n%b
    lst=expansion((n-a0)//b, b)
    lst.insert(0,a0)
    return lst

# 04) Towers of Hanoi



# 05) The Catalan Numbers
# The Catalan numbers a sequence of integers defined inductively via C0=1 and Cn+1=(2(2n+1)/n+2)*Cn for integers n≥0. 
# Define a recursive function catalan(n) which takes as input an integer i≥0 and returns the Catalan number Ci. 
# (The Catalan numbers first appeared as an exercise in the page on Lists.)
def catalan(n):
    if n == 0:
        return 1
    return catalan(n-1)*(2*(2*n+1)/(n+2))
    

# 06) Multiplication using Addition
# Write a recursive function multiply(m,n) which takes as input two integers m and n, and
# returns their product m ∗ n only using addition and subtraction.
# Hints: m ∗ 0 = 0, m ∗ n = m ∗ (n − 1) + m and m ∗ n = m ∗ (n + 1) − m.
# (Remark: Your function should work for all integers.)
def multiply(m,n):
    try:
        if n==0:
            return 0
        elif n==1:
            return m
        elif n < 0:
            return  multiply(m, n+1) - m
        else:
            return multiply(m, n-1) + m
    except Exception as error:
        return error


# 07) Greatest Common Divisor
# Write a recursive function gcd(m,n) which returns the greatest common divisor of 
# integers m≥0 and n≥0 (not both zero). Use the following observations:
# gcd(m,n)=gcd(n,m) for all m and n.
# gcd(0,n)=n when n>0.
# gcd(m,n)=gcd(n%m,m) whenever 0<m≤n.
def gcd(m,n):
    if m==0:
        return n
    elif m>n:
        return gcd(m%n,n)
    return gcd(n%m, m)


# 08) Iteration of a Function
# Suppose f:ℝ→ℝ. Then, we define f^{∘k} to be f applied k∈ℕ times:
# f^{∘k}(x) = f∘f∘…∘f(x)_k for x∈ℝ. Write a recursive function iterate(f,k,x) which takes as
# input a function f:ℝ→ℝ, a natural number k, and a floating point number x and
# returns the value of f^{∘k}(x).
# Example:
# g = lambda x: x**2
# iterate(g,3,1.1) >>> 2.143588810000001
# h = lambda x: 2*x*(1-x)
# iterate(h,100,0.25) >>> 0.5
# for i in range(10): print('[',i,']:', iterate(g,i, 1.1))
g = lambda x: x**2
h = lambda x: 2*x*(1-x)

def iterate(f,k,x):
    try:
        if k > 0:
            if k==1:
                return f(x)
            return iterate(f,k-1,f(x))
        else:
            return 'k is not greater than 1'
    except Exception as error:
        return error

# 09) The Cantor Set 
# The middle third Cantor set is defined by a limiting process. We define C_0 = [0,1] and will define C_i inductively 
# for integers i ≥ 0. Each C_i is a finite union of closed intervals. For each integer i ≥ 0, we define C_i + 1 ⊂ C_i 
# by removing the middle third of the intervals in Ci. So for example
# C1 = [0,1/3] ∪ [2/3,1] and C2 = [0,1/9] ∪ [2/9,1/3] ∪ [2/3,7/9] ∪ [8/9,1].
# The middle third Cantor set is defined by C= ⋂ {from i=0 to ∞} C_i.
# Write a function cantors_set_contains(n,x) which takes as input an integer n ≥ 0 and returns the truth value of the statement x ∈ C_n.
# You do not have to use recursion. But, if you want to use recursion, it might be helpful to use the function f:C_1→C_0 by
# f(x) = 3x, if x ∈ [0,1/3] or 3x−2, if x ∈ [2/3,1].
# Then you can define C_i by iteration:
# Ci={x ∈ [0,1] : {x, f(x), f^{∘2)(x) , … , f{∘(i−1)}(x)} ⊂ C_1}.
# An equivalent way to define C_i is C_i = {x : f{∘i(x)} is well defined}.
# (Can you see why these versions of C_i are correct?)
# Hint: For testing, it may be useful to note that 1/4 ∈ C while 1/2*3^{k} ∉ C for any integer k ≥ 0.
# Example:
# cantors_set_contains(3, 5/6) >>> False
# cantors_set_contains(10, 1/4) >>> True
# for i in range(100): print('[',i,']:', cantors_set_contains2(i, 1/4))
def cantors_set_contains(n,x):
    try:
        if n==0 and (x >= 0 and x <= 1):
            return True
        
        elif n>=1 and (x >= 0 and x <= 1):
            i = 1
            Start = 0; End = 1
            pivot1 = 0; pivot2 = 0
            
            while i <= n:
                interval = (End-Start)/3
                pivot1 = Start+interval
                pivot2 = Start+(2*interval)

                if Start<=x and x<=pivot1:
                    End = pivot1
                elif pivot2<=x and x<=End:
                    Start = pivot2
                else:
                    return False
                i+=1

            if Start <=x and x<=End:
                return True
            else:
                return False
            
        else:
            return False
    except Exception as error:
        return error

def cantors_set_contains_01(n,x):
    if x < 0:
        return False

    if x <= 1:
        # Here we know that x lies in [0,1]
        if n==0:
            return True
        

        if x <= 1/3:
            # Here we know x lies in [0,1/3].
            return cantors_set_contains(n-1, 3*x)
            
        if x < 2/3:
            # Here we know x lies in (1/3, 2/3) and n>1.
            return False

        # Here we know x lies in [2/3, 1].
        return cantors_set_contains(n-1, 3*x-2)

    # Here we know x>1.
    return False

# 10) The Sum of Sequence
# Write a recursive function sum_sequence(f,N) which returns the sum of f(n) from n=0 to N-1.
# Here f should be a function which takes as input an integer and produces a number, and N
# should be an integer bigger than zero. Note that sum_sequence(f,0) should always return zero.
def sum_sequence(f,N):
    if N==0:
        return 0
    return sum_sequence(f,N-1)+f(N-1)


# 11) The Fibonacci Sequence with Recursion
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-2)+fibonacci(n-1)

# Memoization Approach (Dynamic Programming)       
def fibonacci_m(n):
    memo = {0:0, 1:1}
    if not n in memo:
        memo[n] = fibonacci_m(n-1) + fibonacci_m(n-2)
    return memo[n]
