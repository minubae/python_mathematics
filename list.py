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
# Examples:
# tribonacci(100) >>> [0, 0, 1, 1, 2, 4, 7, 13, 24, 44, 81]
# tribonacci(1) >>> [0, 0]
# tribonacci(81) >>> [0, 0, 1, 1, 2, 4, 7, 13, 24, 44]
def tribonacci(m):
    temp=[0]*3
    temp[0] = 0; temp[1] = 0; temp[2] = 1
    res = 0; n = 3
    if m==1:
        temp.remove(m)
    else:
        while res < m:
            res = temp[n-3] + temp[n-2] +temp[n-1]
            if res < m:
                temp.append(res)
            n += 1
    return temp

def tribonacci3(m):
    # TODO:
    # Need to be fixed. More works.
    temp=[0]*3
    if m >= 1:
        temp[0] = 0; temp[1] = 0; temp[2] = 1
        n = 0
        # print('len:',len(temp)-1)
        t = len(temp)-1
        print('temp: ',temp[t])
        if temp[t] < m:
            print('hi good')
            while temp[t] < m:
                res = temp[n] + temp[n+1] + temp[n+2]
                if res < m:
                    temp.append(res)
                    print('res:',res)
                n+=1
        else:
            temp.remove(m)
        return temp
    else:
        return 'm is not greater than equal to 1'
    


# r_tribonacci(10)
def r_tribonacci(n):
    if n==0 or n==1:
        return 0
    elif n==2:
        return 1
    return r_tribonacci(n-3) + r_tribonacci(n-2) + r_tribonacci(n-1)

def tribonacci2(m):
    # TODO:
    # It neens to be fixed when m=1.
    # Which should return a_{0} = 0 and a_{1} = 0 < 1, where a_{k} < m
    
    a, b, c = 0, 0, 1; temp=list()
    temp.append(a); temp.append(b); temp.append(c)
    i = 1
    while i <= m:
        a, b, c = b, c, a + b + c
        if c < m:
            temp.append(c)
        if c >= m:
            temp.remove(c)
        i+=1
    return temp

def fibonacci(n):
    a, b = 0, 1
    temp=list()
    while b < n:
        # print(b, end=',')
        a, b = b, a+b
        temp.append(b)
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
# OUTPUT:
# first few Catalan numbers for n=1, 2, ... are 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, ...
# Examples:
# catalan_numbers(10) >>> [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862]
def binominal_coefficient(n,k):
    res = 1
    if k > (n - k):
        k = n - k
    for i in range(k):
        res = res * (n - i)
        res = res // (i + 1)
    return res

def factorial(n):
    i = 1
    fact = 1
    if n == 0 or n == 1:
        return 1
    while i <= n:
        fact = fact*i
        i += 1
    return fact

def catalan_numbers(n):
    temp=list()
    C = 0
    for i in range(n):
        C = factorial(2*i) // (factorial(i+1)*factorial(i))
        temp.append(C)
    return temp

def catalan_numbers2(n):
    temp=list()
    for i in range (n):
        c = binominal_coefficient(2*i, i)
        temp.append(c // (i+1))
    return temp






