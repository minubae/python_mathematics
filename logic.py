# Title: Mathematical Algorithms - Logic in Python
# Date: Oct/27/2015, Tuesday - Current
# Author: Minwoo Bae (minubae.nyc@gmail.com)
# Reference: http://wphooper.com/teaching/2015-fall-308/python/Logic.html

import math

# 01) The Truth Table
# Suppose truth_function is a function which takes as input two boolean values  P  and  Q  and
# returns a new Boolean value. Then we can print out a truth table for truth_function.
# Here is a function which does this:
def print_truth_table(truth_function):
    print(" P    |  Q    |  ", truth_function.__name__,"(P,Q)", sep="")
    for P in (True, False):
        for Q in (True, False):
            print(str(P).ljust(5), "|", str(Q).ljust(5), "|",str(truth_function(P,Q)).ljust(5))

# 02) The Disjunction
# The disjunction of the statement  P  and  Q  is the statement P or Q and
# is denoted by  P∨Q. Write a function named disjunction(P,Q) that takes
# as input two boolean values  P  and  Q  and returns the truth value of the statement " P or Q".
def disjunction(P,Q):
    return P or Q

# 03) The Conjunction
# The disjunction of the statement  P  and  Q  is the statement P and Q and
# is denoted by  P ∧ Q. Write a function named disjunction(P,Q) that takes
# as input two boolean values  P  and  Q  and returns the truth value of the statement " P and Q".
def conjunction(P,Q):
    return P and Q

# 04) Exclusive Or
# The exclusive or logical operation takes as input Boolean values and returns True or False.
# It returns True if one of the two expressions is true and the other is false (in any order).
# It returns False if the two truth values match. Write a function named xor which takes
# as input two boolean values P and Q and when evaluated as xor(P,Q) returns
# the value of  P xor Q (P⊕Q).
def xor(P,Q):
    return (P or Q) and not (P and Q)


# 05) The Implication
# For statement  P and Q, the implication (or conditional) is the statement If P, then Q
# Write a function named implies(P,Q) that takes as input two boolean values  P and Q
# and returns the truth value of the statement " P implies Q".
def implies(P,Q):
    if(P and Q) or (not P and Q) or (not P and not Q):
        return True
    elif(P and not Q):
        return False
    
# 06) The Biconditional
# For statements (or open sentences)  PP  and  QQ , the conjunction (P⟹Q)∧(Q⟹P)
# of the implication  P⟹Q and its converse is called the biconditional of  P and Q and
# is denoted by  P⟺Q. Write a function named iff(P,Q) that takes as input two boolean values
# P and  Q  and returns the truth value of the statement " P if and only if Q".
def iff(P,Q):
    if (P and Q) or (not P and not Q):
        return True
    elif (not P and Q) or (P and not Q):
        return False
    
# 07) Logical Equivalence
# Let R and S are called logically equivalentlogically equivalent if R and S have the same truth values
# for all combinations of truth values of their component statements.
# If R and S are logically equivalent, then this is denoted by R≡S.
# Write a function named logically_equivalent(tf1, tf2) that takes as input two 2-input truth functions
# tf1 and tf2 and returns the boolean value of the statement ”The two truth functions are logically equivalent.”
# Your function should return True if and only if the two functions tf1 and tf2 return the same output
# whenever they are passed the same input values.
def logically_equivalent(tf1, tf2):
    temp_tf1 = [] # List()
    temp_tf2 = [] # List()
    for P in (True, False):
        for Q in (True, False):
            temp_tf1.append(tf1(P,Q))
            temp_tf2.append(tf2(P,Q))
    return temp_tf1 == temp_tf2

def logically_equivalent_01(tf1, tf2):
    for P in (True, False):
        for Q in (True, False):
            if not iff( tf1(P,Q), tf2(P,Q) ):
                return False
    return True
