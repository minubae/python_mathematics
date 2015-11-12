# Title: Examples of Mathematics Logic and Set in Python
# Date: Oct/27/2015, Tuesday - 
# Author: Minwoo Bae (minubae.nyc@gmail.com)
# Reference: http://wphooper.com/teaching/2015-fall-308/python/Recursion.html

import math

## From Examples:
def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)

## Pascal's triangle:
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

def expansion(n,b):
    if n<b:
        return [n]
    a0 = n%b
    lst=expansion((n-a0)//b, b)
    lst.insert(0,a0)
    return lst

## Example 01
# (Catalan Numbers) The Catalan numbers a sequence of integers defined inductively via C0=1 and Cn+1=2(2n+1)n+2Cn for integers n≥0. 
# Define a recursive function catalan(n) which takes as input an integer i≥0 and returns the Catalan number Ci. 
# (The Catalan numbers first appeared as an exercise in the page on Lists.)

## Example 02
# (Greatest common divisor) Write a recursive function gcd(m,n) which returns the greatest common divisor of 
# integers m≥0 and n≥0 (not both zero). Use the following observations:
# gcd(m,n)=gcd(n,m) for all m and n.
# gcd(0,n)=n when n>0.
# gcd(m,n)=gcd(n%m,m) whenever 0<m≤n.

## Problem 03
# Write a recursive function multiply(m,n) which takes as input two integers m and n, and
# returns their product m ∗ n only using addition and subtraction.
# Hints: m ∗ 0 = 0, m ∗ n = m ∗ (n − 1) + m and m ∗ n = m ∗ (n + 1) − m.
# (Remark: Your function should work for all integers.)
def multiply(m,n):
    if n==0:
        return 0
    elif n==1:
        return m
    else:
        return m + multiply(m, n-1)

## Problem 04
# Suppose f:ℝ→ℝ. Then, we define f^{∘k} to be f applied k∈ℕ times:
# f^{∘k}(x) = f∘f∘…∘f(x)_k for x∈ℝ. Write a recursive function iterate(f,k,x) which takes as
# input a function f:ℝ→ℝ, a natural number k, and a floating point number x and
# returns the value of f^{∘k}(x).
def f(x):
    return x**2

def iterate(f, k, x):
    res = x
    temp=[]
    for i in range(1,k+1):
        res = f(res)
        temp.append(res)
    return temp




















