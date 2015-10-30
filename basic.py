# Title: Examples of Basic Mathematics in Python
# Date: Oct/06/2015, Tuesday
# Author: Minwoo Bae (mbae000@citymail.cuny.edu)
# Reference: http://wphooper.com/teaching/2015-fall-308/python/Numbers.html

import math
# from sympy import * # Import the Sympy library for the computation of Calculus 

## Example 01: 
# Write a Python function print_divisor(p) which takes as input an integer p >= 1 
# and prints all its positive divisors.
def print_divisor(p):
	i=1
	while i < p:
		if p%i == 0:
			print('Divisor: ', i)
		i += 1
# print('Enter an integer number p >= 1: ')
# num1 = int(input())
# print(print_divisor(num1))

## Example 02:
# Write a Python function called factorial(n) which takes as input a positive integer n 
# and return n!.
def factorial(n):
	i = 1
	fact = 1
	if n == 0 or n == 1:
		return 1

	# Recursive solution: 
	# fact = factorial(n-1) * n
	# return fact

	while i <= n:
		fact = fact*i
		i += 1

	return fact

# print('Enter a positive integer n: ')
# num2 = int(input())
# print(factorial(num2))

## Example 03:
# Write a Python function called is_square(n) which takes as input an integer n 
# and returns truth-value of the statement "There is an integer k so that n = k^2".
def is_square(n):
	for k in range(n):
		if k**2 == n:
			return True
	return False

# print('Enter an integer n: ')
# num3 = int(input())
# print(is_square(num3))

## Example 04:
# An approximation to a definite integral of a real valued function is
# ∫ from a to b f(x)dx ≈ (b−a)/n * ∑ from i=0 to n−1 f(a + i(b−a)/n)
# for large values of n. Here is a function which evaluates 
# this sum on an arbitrary function.
def approximate_integral(f, a, b, n):
	step_size = (b-a)/n
	i = 0
	sum = 0
	while i<n:
		sum = sum + f(a+i*(b-a)/n)
		i += 1
	return sum * (b-a) / n

## Example 05:
# Write a function evalf(x,y) which takes two numbers x and y and
# returns the value of the expression f(x,y)=3*x*y + 1 / x**2 + 1.
def evalf(x,y):
        temp = (3*x*y+1) / (x**2 + 1)
        return temp

## Example 06: 
# Write a function called sum_of_cubes(n) which takes as input a positive integer n
# and returns the sum
# 1^3 + 2^3 + 3^3 + ... + n^3 = ∑ from j = 1 to n j^3.
def sum_of_cubes(n):
        temp = 0
        num = n+1
        for i in range(1, num):
                temp = temp + i**3
                print('Sum of Cubes '+str(i)+': ',temp)
        return temp

# Collatz Conjecture
# f(n) = n/2 if n%2==0, 3*n+1 if n%2==1
def collatz(n):
        temp = []
        while n != 1:
                if n%2 == 0:
                        n = n // 2
                elif n%2 == 1:
                        n = 3*n+1
                temp.append(n)

        return temp


