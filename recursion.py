# Title: Examples of Mathematics Logic and Set in Python
# Date: Oct/27/2015, Tuesday - 
# Author: Minwoo Bae (minubae.nyc@gmail.com)
# Reference: http://wphooper.com/teaching/2015-fall-308/python/Recursion.html

import math
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
# (Catalan Numbers) The Catalan numbers a sequence of integers defined inductively via C0=1 and Cn+1=(2(2n+1)/n+2)*Cn for integers n≥0. 
# Define a recursive function catalan(n) which takes as input an integer i≥0 and returns the Catalan number Ci. 
# (The Catalan numbers first appeared as an exercise in the page on Lists.)
def catalan(n):
    if n == 0:
        return 1
    return catalan(n-1)*(2*(2*n+1)/(n+2))
    
## Example 02
# (Greatest common divisor) Write a recursive function gcd(m,n) which returns the greatest common divisor of 
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

## Recursive Fibonacci function:
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-2)+fibonacci(n-1)


## Recursion Test:
def call_me(n):
    if n<=0:
        print("Reached base case of n=", n)
    else:
        print("Function called with n=", n)
        call_me(n-1)
    #print("Exiting call of function with n=", n)

## From Examples:
def factorial(n):
    if n==0:
        return 1
    print('n:',n)
    return n*factorial(n-1)

## Problem 01:
# The tribonacci sequence is a sequence of integers defined inductively by a0 = a1 = 0, a2 = 1, and a_{n+3} = a_{n} + a_{n+1} + a_{n+2}
# for integers n ≥ 0. (a_{n} = a_{n-3} + a_{n-2} + a_{n-1}) Write a function tribonacci(m) which takes as input an number m ≥ 1
# and returns the list [a0, a1, a2, . . . , a_{k}] where ak is the largest number in the sequence with a_{k} < m.
# Examples:
# tribonacci(100) >>> [0, 0, 1, 1, 2, 4, 7, 13, 24, 44, 81]
# tribonacci(1) >>> [0, 0]
# tribonacci(81) >>> [0, 0, 1, 1, 2, 4, 7, 13, 24, 44]
# for i in range(100): print('[',i,']:', tribonacci(i))
def tribonacci(m):
    if m >= 1:
        temp=[0]*3
        temp[0] = 0; temp[1] = 0; temp[2] = 1
        res = 0; n = 3; index = 0
        index = len(temp)-1
        
        while res < m:
            res = temp[n-3] + temp[n-2] +temp[n-1]
            
            if res < m:
                temp.append(res)
            n += 1
            
        if temp[index] >= m:
            temp.remove(temp[index])
        return temp
    else:
        return 'm is not greater than equal to 1'
        
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
# for i in range(100): print('[',i,']:', catalan_numbers(i))
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
    try:
        for i in range(n):
            C = factorial(2*i) // (factorial(i+1)*factorial(i))
            temp.append(C)
        return temp
    except Exception as error:
        return error
    
def catalan_numbers2(n):
    temp=list()
    for i in range (n):
        c = binominal_coefficient(2*i, i)
        temp.append(c // (i+1))
    return temp

## Problem 03
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
    
## Problem 04
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
    
def iterate2(f, k, x):
    try:
        res = x
        for i in range(1,k+1):
            res = f(res)
        return res
    except:
        return 'The procedure was unsuccessful.'

# Problem 05: 
# (Cantor set) The middle third Cantor set is defined by a limiting process. We define C_0 = [0,1] and will define C_i inductively 
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
def cantors_set_contains(n, x):

    def f(x):
        if x >= 0 and x <= 1/3:
            return 3*x
        elif x >= 2/3 and x <= 1:
            return 3*x - 2

    if n == 0:
        if x >= 0 and x <= 1:
            return True
        else:
            return False
        
    elif n == 1:
        if (x >= 0 and x <= 1/3) or (x >= 2/3 and x <= 1):
            return True
        else:
            return False
        
    elif n > 1:
        cantors_set_contains(n-1, f(x))
        if (f(x) >= 0 and f(x) <= 1/3) or (f(x) >= 2/3 and f(x) <= 1):
            return True
        else:
            return False
    else:
        return 'n is not greater than equal to 0.'



def cantors_set_contains2(n,x):
    try:
        if n==0 and (x >= 0 and x <= 1):
            return True
        elif n>=1 and (x >= 0 and x <= 1):
            i = 1
            Start = 0; End = 1
            pivot1 = 0; pivot2 = 0
            
            while i <= n:
                print('start')
                interval = (End-Start)/3
                pivot1 = Start+interval
                pivot2 = Start+(2*interval)

                print('Start:', Start)
                print('pivot1:',pivot1)
                print('x:', x)
                print('pivot2:',pivot2)
                print('End:', End)
                print('')
                
                if Start<=x and x<=pivot1:
                    print('case1')
                    print('')
                    End = pivot1
                elif pivot2<=x and x<=End:
                    print('case2')
                    print('')
                    Start = pivot2
                else:
                    return False
                i+=1
            
            print('Start:', Start)
            print('End:', End)
            print('')
            if Start <=x and x<=End:
                return True
            else:
                return False
            
        else:
            return False
    except Exception as error:
        return error

    
def cantors_set_contains3(n, x):

    def f(x):
        if x >= 0 and x <= 1/3:
            return 3*x
        elif x >= 2/3 and x <= 1:
            return 3*x - 2
        else:
            return x
       
    if n == 0:
        if x >= 0 and x <= 1:
            return True
        else:
            return False
    elif n == 1:
        if (x >= 0 and x <= 1/3) or (x >= 2/3 and x <= 1):
            return True
        else:
            return False
    elif n > 1:
        res = x
        for i in range(1,n+1):
            res = f(res)
        if (res >= 0 and res <= 1/3) or (res >= 2/3 and res <= 1):
            return True
        else:
            return False
    else:
        return 'n is not greater than equal to 0.'












