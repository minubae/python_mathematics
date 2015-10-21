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
    if (P == True and Q == True):
        return True
    elif (P == True and Q == False):
        return False
    elif (P == False and Q == True):
        return True
    elif (P == False and Q == False):
        return True
    return False

###########################################################################
# Problem 02:
# Write a function named iff(P,Q) that takes as input two boolean values P and Q and returns
# the truth value of the statement “P iff Q.”
def iff(P,Q):
    if (P and Q) or (not P and not Q):
        return True
    return False

###########################################################################
# Problem 03:
# Write a function named logically_equivalent(tf1, tf2) that takes as input two 2-input
# truth functions tf1 and tf2 and returns the boolean value of the statement ”The two truth
# functions are logically equivalent.” Your function should return True if and only if the two
# functions tf1 and tf2 return the same output whenever they are passed the same input values.
def logically_equivalent(tf1, tf2):
    for P in (True, False):
        for Q in (True, False):
            if iff(tf1(P,Q), tf2(P,Q)):
                return True
            else:
                return False
    return False

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
