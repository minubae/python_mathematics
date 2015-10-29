# Title: Examples of Mathematics Logic and Set in Python
# Date: Oct/27/2015, Tuesday
# Author: Minwoo Bae (minubae.nyc@gmail.com)
# Reference: http://wphooper.com/teaching/2015-fall-308/python/Logic.html
#                    http://wphooper.com/teaching/2015-fall-308/python/Tuples_and_Sets.html
import math

# Lambda Example:
numbers = list(range(1,11))
square = lambda x: x**2
square_list = list(map(square, numbers))

# Exclusive (Logic)
def xor(P,Q):
    return (P or Q) and not (P and Q)

## Example 01: 
# A divisor of an integer n, is an integer d so that d divides n, i.e., so that n/d ∈ ℤ. 
# Write a function whose name is divisors which takes as input an integer n and returns 
# the set of positive divisors of n.
def divisors(n):
    divisor_set = set()
    for d in range(n):
        if d != 0 and n%d == 0:
            divisor_set.add(d)
    return divisor_set

## Example 02:
# Using the previous problem, write an function named gcd2 which takes as input two positive integers a 
# and b and returns their greatest common divisor. Instead of using Euclid's algorithm, use the previous 
# part to compute the two sets of divisors of the numbers. Then intersect these sets and
# find the maximal element. 
# Note that in Python, you can write max(S) to find the maximal element of the set S. 
# (Remark: This function is much more inefficient than Euclid's algorithm!)
def gcd(a,b):
    if a>b:   # Ensure that a<=b:
        (a,b) = (b,a)  # Swap the values of a and b if a>b.
    while a!=0:
        (a,b) = (b%a,a)
    return b

def minu_gcd(a,b):

    gcd_set = set()
    temp_a = set()
    temp_b = set()
    
    for d in range(a):
        if d !=0 and a%d == 0:
            temp_a.add(d)

    for d in range(b):
        if d !=0 and b%d == 0:
            temp_b.add(d)

    # A & B, A.intersection(B) : Returns the intersection of A and B.
    gcd_set = temp_a & temp_b
    # gcd_set = temp_a.intersection(temp_b)

    # A | B, A.union(B) : Returns the union of A and B.
    # A - B, A.difference(B) : Returns the set-theoretic difference A \ B.
    # A <= B, A.issubset(B) : Returns the boolean value of the statement A is a subset of B.
    # A >= B, A.issuperset(B) : Returns the boolean value of the statement A contains B.
    # A == B, Tests of equality of sets returning a boolean value.

    gcd_set = sorted(gcd_set)
    return minu_max(gcd_set)

## Example 03:
# Write a function named intersection which takes as input two sets A and B and returns 
# the intersection of A and B. Do not use the intersection methods defined by Python. 
# You should be able to do this with the set() function for constructing the empty set, 
# one for loop for looping through elements of a set, the in statement for testing membership, 
# and the add method for adding elments to a set.
def minu_intersection(A, B):
    temp_set = set()
    for a in A:
        for b in B:
            if a == b:
                temp_set.add(a)
    
    return sorted(temp_set)

def minu_union(A, B):
    U = set()
    for a in A:
        U.add(a)

    for b in B:
        U.add(b)

    return sorted(U)

## Example 04:
# Write your own function named max2 which takes as input a tuple t of numbers and 
# returns the maximal element of t. Do not use the max function mentioned above, 
# instead loop through the elements of t to find the maximal element.
def minu_max(S):
    temp_max = 0
    for e in S:
        if e > temp_max:
            temp_max = e
    return temp_max

## Example 05:
# Write a function set_of_squares(n) which takes as input a natural number n and returns the set
# An = {k^2: k ∈ ℤ and 0 ≤ k ≤ n}.
def set_of_squares(n):
    temp_set = set()
    
    for k in range(n+1):
        temp_set.add(k**2)
        
    return sorted(temp_set)

## Example 06:
# For sets of numbers A and B, let A⊕B denote their sumset as defined two problems above. 
# For n ∈ ℕ, let An be as in the previous problem. Use the functions defined in the two prior problems to 
# compute (An ⊕ An) ⊕ (An ⊕ An) for small values of n. Let A∞ = {k^2: k ∈ ℤ}. Use the results of this calculation 
# to formulate a conjecture about the nature of the set (A∞ ⊕ A∞)⊕(A∞ ⊕ A∞).
# (Remark. Sets in Python are sometimes printed out of order. If you have a set X and want to see it in order, 
# you can first convert it to a list with L=list(X). Then you can sort it with L.sort(). 
# Then printing L printes the members of X in order. Lists will be covered soon.)


## Example 07:
# Lagrange's four-square theorem states that any non-negative integer is the sum of the squares of four integers. 
# Write a function lagrange_four_square(n) which takes as input a non-negative integer n and returns a quadruple (a,b,c,d) of integers 
# so that n = a^2+b^2+c^2+d^2.
def lagrange_four_square(n):
    quadruple = set()
    return quadruple

## Example 08:
# Suppose A, B and C are subsets of ℤ. Consider the quantified statement ⋆:∀a ∈ A ∃b ∈ B such that a−b ∈ C.
# Write a function called verify_star which takes as input three sets of integers A, B and C and 
# returns the truth-value of ⋆ (i.e., returns True or False depending on the truth value of ⋆ in this case).
def verify_star(A, B, C):
    result = False
    return result

## Example 09:
# Let ϵ > 0. Say that a triangle is ϵ-nearly equilateral if for any two side lengths of the triangle s1 and s2, 
# the ratio s1/s2 is less than 1+ϵ. Write a function is_nearly_equilateral(P,Q,R,epsilon) which takes as input three points 
# in the plane P, Q and R as well as a positive parameter epsilon and returns the truth-value of the statement 
# "The triangle PQR is epsilon-nearly equilateral. (Remark: Why is unreasonable to use a function called is_equilateral(P,Q,R) 
# which returns the truth-value of "The triangle PQR is equilateral?")
def is_nearly_equilateral(P,Q,R,epsilon):
    result = False
    return result

## Example 10:
# Write a function is_square which takes as input four points in the plane with integer coordinates and returns 
# the truth-value of the statement "The four points are the vertices of a square."
def is_square(pointSet):
    result = False
    return result

## Example 11 (Fibonacci Numbers):
# F(n) = F(n-1)+F(n-2), n>=3, F(0)=0, F(1)=1

# Iteration Approach: Very Fast
# To calculate the nth Fibonacci number in only n steps,
# we can also start with 0 and 1 and iteratively add up items n times:
def fibonacci(n):
    a, b = 0, 1
    while b < n:
        print(b, end=',')
        a, b = b, a+b

# Recursive Approach: takes lots of time to solve it
def fibonacci_r(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_r(n-1) + fibonacci_r(n-2)

# Memoization Approach:       
def fibonacci_m(n):
    memo = {0:0, 1:1}
    if not n in memo:
        memo[n] = fibonacci_m(n-1) + fibonacci_m(n-2)
    return memo[n]












