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

## Problem 01:
# The tribonacci sequence is a sequence of integers defined inductively by a0 = a1 = 0, a2 = 1, and a_{n+3} = a_{n} + a_{n+1} + a_{n+2}
# for integers n ≥ 0. (a_{n} = a_{n-3} + a_{n-2} + a_{n-1}) Write a function tribonacci(m) which takes as input an number m ≥ 1
# and returns the list [a0, a1, a2, . . . , a_{k}] where ak is the largest number in the sequence with a_{k} < m.
def tribonacci(m):
    if m == 0 or m == 1:
        return 0
    elif m == 2:
        return 1
    return tribonacci(m-3) + tribonacci(m-2) + tribonacci(m-1)

def tribonacci_01(m):
    a, b, c = 0, 0, 1; temp=list()
    temp.append(a); temp.append(b); temp.append(c)
    while c < m:
        a, b, c = b, c, a + b + c
        temp.append(c)
    return temp

def tribonacci_02(n):
    last = 1
    secondLast = 1
    thirdLast = 1
    temp=list()
    for i in range(2,n):
        new = last + secondLast + thirdLast
        thirdLast = secondLast
        secondLast = last
        last = new
        temp.append(last)
    return temp

## Problem 02:
# Viewing addition as a binary operation, the Catalan number Ck is the number of ways to write k+1 as a sum of k+1 ones.
# Here k≥0 is an integer. For example C0=1 because 1 can only be expressed as 1, and C1=1 because 2=1+1 is
# the only way to write 2 as a sum of ones. But, C2=2 because 3=(1+1)+1=1+(1+1), and C3=5
# because 4=1+(1+(1+1))=1+((1+1)+1)=(1+1)+(1+1)=((1+1)+1)+1=(1+(1+1))+1.
# Suppose we have an expression for k+1 as a sum of ones. Then there is an outermost addition, and
# we can simplify the left and right sides. For example, the sum (1+(1+1))+1 simplifies to 3+1.
# Every sum representing k+1 simplifies to a sum of the form a+b with a≥1, b≥1 and a+b=k+1.
# Furthermore in such a sum a and b are each represented as a sum of ones. It follows that for k≥1 we have
# C_k=∑(i=0, k−1) Ci * C_(k−i−1).
# (Here each term Ci * C_(k−i−1) represents number of ways to write k+1 as a sum of ones which simplifies to (i+1)+(k−i).)
# Write a function catalan_numbers(n) which returns the list of the first n Catalan numbers:
# [C0, C1, . . . , Cn−1]. Remark: All you really need to know about the Catalan numbers is that C0 = 1 and
# the summation formula above.
# (The Catalan numbers show up in a lot of counting problems. Wikipedia has a nice article on the Catalan numbers.)
def catalan_numbers(n):
    C = list()
    r = 0
    if  n <= 1:
        return 1
    
    for i in range(n):
        r += catalan_numbers(i)*catalan_numbers(n-i-1)

        #print(r)
        C.append(r)
    return C

def catalan_numbers2(n):
    #catalan = [0 for i in range(n+1)]
    catalan = [0] * (n+1)
    res = 0
    for x in range(2):
            catalan[x] = 1
    print(catalan)
    
    for i in range(2,n):
        catalan[i] = 0
        for j in range(i):
            res = catalan[i] + (catalan[j] * catalan[i-j-1])
            #print(catalan[i])
    return res

# OUTPUT:
# first few Catalan numbers for n=1, 2, ... are 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, ... 
def catalan_numbers3(n):
    
    temp=list()
    
    def binominal_coefficient(n,k):
        res = 1
        if k > (n - k):
            k = n - k
        for i in range(k):
            res *= (n - i)
            res //= (i + 1)
        return res
    
    for i in range (n+1):
        c = binominal_coefficient(2*i, i)
        temp.append(c // (i+1))
    return temp









