# Title: Examples of Mathematics List in Python
# Date: Nov/02/2015, Monday - 
# Author: Minwoo Bae (minubae.nyc@gmail.com)
# Reference: http://wphooper.com/teaching/2015-fall-308/python/Lists.html

def fibonacci_list(n):
    flist = [1,1]
    while len(flist)<n:
        flist.append(flist[len(flist)-1]+flist[len(flist)-2])
    return flist

    
## Example 01
# A list is a palindrome if it is the same when reversed. Write a function is_palindrome(lst) which takes as input a list lst and 
# returns the truth value of the statement "lst is a palindrome."
def is_palindrome(lst):
	return 1
## Example 02
# Write a function derivative(c) which takes as input a list c coefficients of a polynomial and returns the coefficient list of 
# the derivative of the polynomial.
def derivative(c):
	return 1

## Example 03
# Write a function multiply_polynomials(c1,c2) which takes as input two lists of coefficients of two polynomials and 
# returns the coefficient list of the product of these polynomials.
def multiply_polynomials(c1,c2):
	return 1

## Example 04
# A polygon in the plane can be stored as a list of coordinates of vertices, where each vertex is a pair of numbers. 
# For instance [(0,0),(3,0),(0,4)] represents a 3-4-5 right triangle.
# Write a function perimeter(p) which computes the perimeter of the polygon p, where p is represented as a list of coordinates as above. 
# For example, perimeter([(0,0),(3,0),(0,4)]) should return 12 (which is 3+4+5).
def perimeter(p):
	return 1