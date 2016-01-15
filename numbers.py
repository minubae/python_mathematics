# Title: Mathematical Algorithms Basics in Python
# Date: Oct/06/2015, Tuesday - Current
# Author: Minwoo Bae (minubae.nyc@gmail.com)
# Reference: http://wphooper.com/teaching/2015-fall-308/python/Numbers.html

import math

# 01) Find Divisors of a Natural Number P 
# Write a Python function print_divisor(p) which takes as input an integer p >= 1 and prints all its positive divisors.

# Using while_statement
def print_divisor_01(p):
        i=1
        temp=list()
        while i < p:
                if p%i == 0:
                        temp.append(i)
                i += 1
        return temp

# Using for_statement
def print_divisor_02(p):
        temp=list()
        for i in range(1,p):
                if p%i == 0:
                        temp.append(i)
        return temp

# 02) Find a Factorial of a Non-negative Integer N
# Write a Python function called factorial(n) which takes as input a positive integer n and return n!.

# Using while_statement
def factorial_01(n):
        i = 1
        fact = 1
        if n==0 or n==1:
                return 1
        while i<=n:
                fact = fact*i
                i+=1
        return fact

# Using for_statement
def factorial_02(n):
        fact = 1
        if n==0 or n==1:
                return 1
        for i in range(1,n+1):
                fact = fact*i
        return fact

# 03) Is_Square(n), n is a Non-negative Integer Number
# Write a Python function called is_square(n) which takes as input an integer n
# and returns truth-value of the statement "There is an integer k so that n = k^2".
def is_square(n):
        for k in range(n):
                if k**2 == n:
                        return True
        return False

# 04) Sum of Cubes of a Positive Integer n 
# Write a function called sum_of_cubes(n) which takes as input a positive integer n
# and returns the sum 1^3 + 2^3 + 3^3 + ... + n^3 = ∑ from j = 1 to n j^3.
def sum_of_cubes(n):
        temp = 0
        num = n+1
        for i in range(1, num):
                temp = temp + i**3
        return temp

# 05) Find a Slope of a Secent Line
# Functions can be passed to functions which allows them to solve more general problems.
# The following function secant_slope will take as input a real valued function  f:ℝ→ℝf:ℝ→ℝ
# and two input values x1 and x2 and produce the slope of the associated secant line (the line joining (x1, f(x1)) to (x1, f(x1)) ).
def secant_slope(f, x1, x2):
        return (f(x1)-f(x2))/(x1-x2)

# 06) Find an Area of a Triangle from its Three Side Lengths
# The following function computes the area of a triangle from its three side lengths.
# This is the semiperimeter formula for area of a triangle.  Heron's formulaHeron's formula states
# that the area of a triangle whose sides have lengths a, b, and c is:
# A = sqrt(s*(s-a)(s-b)(s-c)), where s = a+b+c / 2
def area(a, b, c):
        s = (a+b+c)/2
        return math.sqrt(s*(s-a)*(s-b)*(s-c))

# 07) Check that a Natural Number p is a Prime Number
# An integer p >= 2 is prime if the only positive numbers which divide it
# evenly are itself and one. 
# Write a funuction is_prime(p) which takes as input an integer p >= 2 and
# returns True if p is prime and False if p is not prime.
# Hints: The number p is not prime if and only if there ia n with 2 <= n < p
# so that the remainder when dividing p by n is zero.
def is_prime(p):
    if p < 2:
        return False
    else:
        for i in range(2,p-1):
            if p%i == 0:
                return False
            else:
                return True

# 08) A Root finding Algorithm with the Newton's Method
# Newton's method is a very efficient way to find a root of a differentiable 
# function f starting with a point near the root. The method gives a sequence
# x0, x1, x2,... of numbers which rapidly approach the root if the initial
# point is sufficiently close to the root. The value x0 is the starting point. 
# Given xk the value of xk+1 by intersecting the x-axis with tangent line to 
# the graph of f at the point (xk, f(fk)). That is, 
# xk+1 = xk - f(xk)/f'(xk).
# An illustration of this process is shown at the end of this question. 
# Write a function newtons_method(f, df, x0, n) which takes as input a function
# f:R ---> R, its derivative df = f' (alse a function from R to R), an initial
# point x0 and an integer n >= 1. The function should return the value xn obtained
# by iterating Newton's method n times.

def f(x):
    return 2-x**2

def df(x):
    return -2*x

# Using while_statement
def newtons_method(f, df, x0, n):
    i = 1
    while i <= n:
        if df(x0) == 0:
            return x0
        x = x0 - f(x0)/df(x0)
        x0 = x
        i+=1
    return x

# Using for_statement
def newtons_method_01(f, df, x0, n):
    for i in range(1, n+1):
        if df(x0) == 0:
            return x0
        x = x0 - f(x0)/df(x0)
        x0 = x
    return x

# 09) Collatz Conjecture
# The Collatz conjecture can be summarized as follows. Take any natural number  n .
# If n is even, divide it by 2 to get  n2 . If n is odd, multiply it by 3 and add 1 to obtain  3n+1 .
# Repeat the process (which has been called "Half Or Triple Plus One", or HOTPO[6]) indefinitely.
# The conjecture is that no matter what number you start with, you will always eventually reach 1.
# The property has also been called oneness. In modular arithmetic notation, define the function f as follows:
# f(n) = n/2 if n%2==0, 3*n+1 if n%2==1
def collatz(n):
    temp = list()
    while n!=1:
        if n%2==0:        
            n = n//2
            temp.append(n) 
        else:
            n = 3*n+1
            temp.append(n) 

    return temp

# 10) An approximation to a definite integral
# An approximation to a definite integral of a real valued function is
# ∫ from a to b f(x)dx ≈ (b−a)/n * ∑ from i=0 to n−1 f(a + i(b−a)/n)
# for large values of n. Here is a function which evaluates 
# this sum on an arbitrary function.

# Using while_statement
def approximate_integral(f, a, b, n):
    h = (b-a)/n
    i = 0
    sum = 0
    while i<n:
        sum = sum + f(a+i*(b-a)/n)
        i += 1
    return sum * (b-a) / n

# Using for_statement
def approximate_integral_01(f, a, b, n):
    h = (b-a)/n
    sum = 0
    for i in range(n):
        sum = sum + f(a+i*(b-a)/n)
    return sum * (b-a) / n






