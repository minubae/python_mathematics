# Subject: Bridge to Advanced Mathematics (Math 308), the City College of New York, CUNY
# Instructor: Prof. Hooper
# Title: Programming Assignment 02 (included 'pa2.py' file)
# Due Date: Oct/20/2015, Thursday
# Author: Minwoo Bae (mbae000@citymail.cuny.edu)

# Problems:
# Inside the file pa2.py place functions as described below which solve each of the
# following problems. Only include these three functions, and be sure to title them as described in
# the problems. (Improperly titled functions will not be called properly.) To write these functions,
# it should be sufficient to understand the documents on Logic and on Tuples and Sets listed on the
# course programming page.

###########################################################################
# Problem 01: 
# Write a function named implies(P,Q) that takes as input two boolean values P and Q and
# returns the truth value of the statement “P implies Q.” (You can test your function using the
# print_truth_table function given on the Logic page.)




###########################################################################
# Problem 02:
# Write a function named iff(P,Q) that takes as input two boolean values P and Q and returns
# the truth value of the statement “P iff Q.”

###########################################################################
# Problem 03:
# Say that a 2-input truth function is a function which takes as input two boolean values P and
# Q and returns a boolean value.( Examples include xor above, as well as implies and iff from the
# problems above.)
# Write a function named logically_equivalent(tf1, tf2) that takes as input two 2-input
# truth functions tf1 and tf2 and returns the boolean value of the statement ”The two truth
# functions are logically equivalent.” Your function should return True if and only if the two
# functions tf1 and tf2 return the same output whenever they are passed the same input values.

###########################################################################
# Problem 04:   
# Write a function planar_distance(p,q) which takes as input two points in the plane and
# returns the distance between them. Here a point in the plane should be interpreted as a 2-tuple
# whose entries are both real numbers.

###########################################################################
# Problem 05: 
# Suppose A and B are two sets of numbers. Their sumset is the set
# {a + b : a ∈ A and b ∈ B}.
# Write a function called sumset(A,B) which takes as input two sets of numbers A and B and
# returns their sumset.