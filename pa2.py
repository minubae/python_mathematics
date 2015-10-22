# Subject: Bridge to Advanced Mathematics (Math 308), the City College of New York, CUNY
# Instructor: Prof. Hooper
# Title: Programming Assignment 02 (included 'pa2.py' file)
# Due Date: Oct/22/2015, Thursday
# Author: Minwoo Bae (mbae000@citymail.cuny.edu)

# Problems:
# Inside the file pa2.py place functions as described below which solve each of the
# following problems. Only include these three functions, and be sure to title them as described in
# the problems. (Improperly titled functions will not be called properly.) To write these functions,
# it should be sufficient to understand the documents on Logic and on Tuples and Sets listed on the
# course programming page.

import math

###########################################################################
# Sample functions for the purpose of testing
def print_truth_table(truth_function):
    print(" P    |  Q    |  ", truth_function.__name__,"(P,Q)", sep="")
    for P in (True, False):
        for Q in (True, False):
            print(str(P).ljust(5), "|", str(Q).ljust(5), "|",str(truth_function(P,Q)).ljust(5))

def or_not(P,Q):
    return (not P) or (not Q)

def not_and(P,Q):
    return not (P and Q)

def or_function(P,Q):
    return P or Q
            
###########################################################################
# Problem 01: 
# Write a function named implies(P,Q) that takes as input two boolean values P and Q and
# returns the truth value of the statement “P implies Q.” (You can test your function using the
# print_truth_table function given on the Logic page.)
def implies(P,Q):
    if(P and Q) or (not P and Q) or (not P and not Q):
        return True
    elif(P and not Q):
        return False

###########################################################################
# Problem 02:
# Write a function named iff(P,Q) that takes as input two boolean values P and Q and returns
# the truth value of the statement “P iff Q.”
def iff(P,Q):
    if (P and Q) or (not P and not Q):
        return True
    elif (not P and Q) or (P and not Q):
        return False

###########################################################################
# Problem 03:
# Write a function named logically_equivalent(tf1, tf2) that takes as input two 2-input
# truth functions tf1 and tf2 and returns the boolean value of the statement ”The two truth
# functions are logically equivalent.” Your function should return True if and only if the two
# functions tf1 and tf2 return the same output whenever they are passed the same input values.
def logically_equivalent(tf1, tf2):
    temp_tf1 = []
    temp_tf2 = []
    for P in (True, False):
        for Q in (True, False):
            temp_tf1.append(tf1(P,Q))
            temp_tf2.append(tf2(P,Q))
    return temp_tf1 == temp_tf2       

###########################################################################
# Problem 04:   
# Write a function planar_distance(p,q) which takes as input two points in the plane and
# returns the distance between them. Here a point in the plane should be interpreted as a 2-tuple
# whose entries are both real numbers.
def planar_distance(p,q):
    x1,y1 = p
    x2,y2 = q
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

###########################################################################
# Problem 05: 
# Suppose A and B are two sets of numbers. Their sumset is the set
# {a + b : a ∈ A and b ∈ B}.
# Write a function called sumset(A,B) which takes as input two sets of numbers A and B and
# returns their sumset.
def sumset(A,B):
    temp_set = set()
    for a in A:
        for b in B:
            temp_set.add(a+b)
    return temp_set

## Example 01: 
# A divisor of an integer n, is an integer d so that d divides n, i.e., so that n/d ∈ ℤ. 
# Write a function whose name is divisors which takes as input an integer n and returns 
# the set of positive divisors of n.
def divisors(n):
    d = 0
    return d

## Example 02:
# Using the previous problem, write an function named gcd2 which takes as input two positive integers a 
# and b and returns their greatest common divisor. Instead of using Euclid's algorithm, use the previous 
# part to compute the two sets of divisors of the numbers. Then intersect these sets and find the maximal element. 
# Note that in Python, you can write max(S) to find the maximal element of the set S. 
# (Remark: This function is much more inefficient than Euclid's algorithm!)
def gcd(a,b):
    if a>b:   # Ensure that a<=b:
        (a,b) = (b,a)  # Swap the values of a and b if a>b.
    while a!=0:
        (a,b) = (b%a,a)
    return b

def gcd2(a,b):
    gcd = 0
    return gcd

def max(S):
    max_element = 0
    return max_element

## Example 03:
# Write a function named intersection which takes as input two sets A and B and returns 
# the intersection of A and B. Do not use the intersection methods defined by Python. 
# You should be able to do this with the set() function for constructing the empty set, 
# one for loop for looping through elements of a set, the in statement for testing membership, 
# and the add method for adding elments to a set.
def intersection(A, B):
    tempSet = set()
    return tempSet

## Example 04:
# Write your own function named max2 which takes as input a tuple t of numbers and 
# returns the maximal element of t. Do not use the max function mentioned above, 
# instead loop through the elements of t to find the maximal element.
def max(t):
    max_element = 0
    return max_element

## Example 05:
# Write a function set_of_squares(n) which takes as input a natural number n and returns the set
# An={k^2: k ∈ ℤ and 0 ≤ k ≤ n}.
def set_of_squares(n):
    temp_set = set()
    return temp_set

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












