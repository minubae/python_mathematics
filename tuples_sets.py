# Title: Mathematical Algorithms - Tuples and Sets in Python
# Date: Oct/27/2015, Tuesday - Current
# Author: Minwoo Bae (minubae.nyc@gmail.com)
# Reference: http://wphooper.com/teaching/2015-fall-308/python/Tuples_and_Sets.html

import math

# Lambda Example:
numbers = list(range(1,11))
square = lambda x: x**2
square_list = list(map(square, numbers))

##########################################################################################################
###********************************************** Tuples **********************************************###
##########################################################################################################
#  01) Baricenter
# The baricenter of a triangle is the average of its coordinates. The following computes the baricenter of a triangle
# (given as a 3-tuple of vertices). This point is always inside the triangle.
def baricenter(triangle):
    p,q,r = triangle    # Store the vertices in p, q and r.
    x1,y1 = p           # Store the coordinates of p in x1 and y1.
    x2,y2 = q
    x3,y3 = r
    return (x1+x2+x3)/3, (y1+y2+y3)/3    # return the average

#  02) The Finonacci Numbers using pairs (a tuple)
# F(n) = F(n-1)+F(n-2), n>=3, F(0)=0, F(1)=1
# To calculate the nth Fibonacci number in only n steps,
# we can also start with 0 and 1 and iteratively add up items n times:
def fibonacci(n):
    a, b = 0, 1
    while b < n:
        print(b, end=',')
        a, b = b, a+b

# 03) Average of numbers in a tuple
# The following computes the average of a students grades provided as a tuple.
def average(grades):
    total = 0
    for grade in grades:
        total =  total + grade
    return total/len(grades)

# 04) Concatenation of tuples:
# You can concatenate (stick together) two tuples with the + operation.
v = 1,3,5
w = 2,4,6
x = v+w
print("The concatenation of v and w is", x)

# 05) The Distance between two Points in the Plane
# Write a function planar_distance(p,q) which takes as input two points in the plane and returns the distance between them.
# Here a point in the plane should be interpreted as a 2-tuple whose entries are both real numbers.
def planar_distance(p,q):
    x1,y1 = p
    x2,y2 = q
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)


##########################################################################################################
####********************************************** Sets **********************************************####
##########################################################################################################

# 01) The Union of a Collection of Sets
# In set theory, the union (denoted by  ∪∪ ) of a collection of sets is the set of all distinct elements in the collection.
# It is one of the fundamental operations through which sets can be combined and related to each other.
# The union of two sets A and B is the set of elements which are in A, in B, or in both A and B.
def union(A,B):
    C=set()         # Define C as the empty set
    for a in A:
        C.add(a)
    for b in B:
        C.add(b)
    return C

# 02) The Intersection of a Collection of Sets
# Write a function named intersection which takes as input two sets A and B and returns the intersection of A and B.
# Do not use the intersection methods defined by Python. You should be able to do this with the set() function for constructing
# the empty set, one for loop for looping through elements of a set, the in statement for testing membership,
# and the add method for adding elments to a set.
def intersection(A, B):
    temp_set = set()
    for a in A:
        for b in B:
            if a == b:
                temp_set.add(a)
    return sorted(temp_set)

# 03) A Subset
# Write a function called is_subset which takes two sets A and B and returns True
# if A is a subset of B and returns False if A is not a subset of B.
def is_subset(A,B):
    for a in A:
        if a not in B:
            return False
    return True

# 04) Sumset of two sets of numbers
# Write a function called sumset(A,B) which takes as input two sets of numbers A and B
# and returns their sumset
def sumset(A,B):
    temp_set = set()
    for a in A:
        for b in B:
            temp_set.add(a+b)
    return temp_set

# 05) Find a Set of Divisors of a Integer number n
# A divisor of an integer n, is an integer d so that d divides n, i.e., so that  n/d ∈ ℤ.
# Write a function whose name is divisors which takes as input an integer n and
# returns the set of positive divisors of n.
def divisors(n):
    divisor_set = set()
    for d in range(n):
        if d != 0 and n%d == 0:
            divisor_set.add(d)
    return divisor_set


# 06) The Greatest Common Divisor of two Natural Numbers a and b
# Using the previous problem, write an function named gcd_02( ) which takes as input two positive integers a 
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

def gcd_02(a,b):

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
    return find_max(gcd_set)

# 07) The Sum of squares
# The following is a simple function which checks if a integer n can be written as a sum of two squares of integers a and b,
# n=a^2+b^2.  It will return such a pair (a,b) if n can be written as a sum of squares and will return None if it can not.
def sum_of_squares(n):
    a=0
    while a**2<=n:
        b=0
        while a**2+b**2<=n:
            if a**2+b**2==n:
                return (a,b)
            b=b+1
        a=a+1
    return None

def print_sum_of_squares(n):
    output = sum_of_squares(n)
    if output is None:
        print(n,"is not a sum of squares.")
    else:
        # Now we know the output is a pair of integers.
        (a,b) = output
        print(n," = ",a,"^2 + ",b,"^2.", sep="")


# 08) The Cartestian Product
# The Cartestian product of two sets  AA  and  BB  is the collection of pairs (a,b) where  a∈A and  b∈B.
# Write a function which takes as input two sets, and returns their Cartesian product.
def cartesian_product(A,B):
    C = set()                # C is the empty set
    for a in A:
        for b in B:
            C.add( (a,b) )
    return C

# 09) Find a Maximum element of a Set
# Write your own function named max2 which takes as input a tuple t of numbers and 
# returns the maximal element of t. Do not use the max function mentioned above, 
# instead loop through the elements of t to find the maximal element.
def find_max(S):
    temp_max = 0
    for e in S:
        if e > temp_max:
            temp_max = e
    return temp_max


# 10) Find a Set of Squares
# Write a function set_of_squares(n) which takes as input a natural number n and returns the set
# An = {k^2: k ∈ ℤ and 0 ≤ k ≤ n}.
def set_of_squares(n):
    temp_set = set()
    
    for k in range(n+1):
        temp_set.add(k**2)
        
    return sorted(temp_set)

# 11) The Lagrange's four-square theorem
# Lagrange's four-square theorem states that any non-negative integer is the sum of the squares of four integers. 
# Write a function lagrange_four_square(n) which takes as input a non-negative integer n and returns
# a quadruple (a,b,c,d) of integers 
# so that n = a^2+b^2+c^2+d^2.
def lagrange_four_square(N):
    tempN = N
    for a in range(tempN,-1,-1):
        for b in range(tempN, -1, -1):
            for c in range(tempN, -1, -1):
                for d in range(tempN, -1, -1):
                    #tempN = tempN - (a**2+b**2+c**2+d**2)
                    if a**2+b**2+c**2+d**2 == N:
                        return a,b,c,d

# 12) Check a Rectangle is a Square
# Write a function is_square which takes as input four points in the plane with integer coordinates and returns 
# the truth-value of the statement "The four points are the vertices of a square."
# INPUT: square = (0, 0), (2, 0), (0, 2), (2,2) = a,b,c,d
# OUTPUT: True
# Properties of a Square:
# - a rectangle with two adjacent equal sides
# - a quadrilateral with four equal sides and four right angles
# - a parallelogram with one right angle and two adjacent equal sides
# - a rhombus with a right angle
# - a rhombus with all angles equal
# - a quadrilateral where the diagonals are equal and are the perpendicular bisectors of each other, i.e. a rhombus with equal diagonals
def is_square(sqaure):
    
    a,b,c,d=square
    m = center_coord(a,b,c,d)
    
    def dist(p1,p2):
        x1, y1 = p1
        x2, y2 = p2
        
        # math.hypot(x, y):
        # Return the Euclidean norm, sqrt(x*x + y*y). This is the length of the vector from the origin to point (x, y)
        return math.hypot(x2-x1, y2-y1)
        # return math.sqrt((x2-x1)**2+(y2-y1)**2)

    def angle(p1,p2):
        x1, y1 = p1
        x2, y2 = p2
        return math.atan2(y2-y1, x2-x1)
    
    if dist(a,b) == dist(a,c)==dist(b,d)==dist(c,d) and dist(a,m) == dist(b,m) == dist(c,m) == dist(d,m):
        return True
    
    return False

def center_coord(p1, p2, p3, p4):
        x1, y1 = p1; x2, y2 = p2
        x3, y3 = p3; x4, y4 = p4

        coord = (x1+x2+x3+x4)/4, (y1+y2+y3+y4)/4

        return coord






    
## Example
# For sets of numbers A and B, let A⊕B denote their sumset as defined two problems above. 
# For n ∈ ℕ, let An be as in the previous problem. Use the functions defined in the two prior problems to 
# compute (An ⊕ An) ⊕ (An ⊕ An) for small values of n. Let A∞ = {k^2: k ∈ ℤ}. Use the results of this calculation 
# to formulate a conjecture about the nature of the set (A∞ ⊕ A∞)⊕(A∞ ⊕ A∞).
# (Remark. Sets in Python are sometimes printed out of order. If you have a set X and want to see it in order, 
# you can first convert it to a list with L=list(X). Then you can sort it with L.sort(). 
# Then printing L printes the members of X in order. Lists will be covered soon.)
def set_calculation(n):
    A = set()
    return A
                    
## Example
# Suppose A, B and C are subsets of ℤ. Consider the quantified statement ⋆:∀a ∈ A ∃b ∈ B such that a−b ∈ C.
# Write a function called verify_star which takes as input three sets of integers A, B and C and 
# returns the truth-value of ⋆ (i.e., returns True or False depending on the truth value of ⋆ in this case).
def verify_star(A, B, C):
    result = False
    return result

## Example
# Let ϵ > 0. Say that a triangle is ϵ-nearly equilateral if for any two side lengths of the triangle s1 and s2, 
# the ratio s1/s2 is less than 1+ϵ. Write a function is_nearly_equilateral(P,Q,R,epsilon) which takes as input three points 
# in the plane P, Q and R as well as a positive parameter epsilon and returns the truth-value of the statement 
# "The triangle PQR is epsilon-nearly equilateral. (Remark: Why is unreasonable to use a function called is_equilateral(P,Q,R) 
# which returns the truth-value of "The triangle PQR is equilateral?")
def is_nearly_equilateral(P,Q,R,epsilon):
    result = False
    return result
