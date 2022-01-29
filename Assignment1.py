"""Python for Visual Effects.

Assignment #1 - Data Types and Variables

Answer the following questions.
"""

# 1.- Make a program that solves and shows the summation of 64 + 32
from itertools import count


mysum = 64 + 32 
print(mysum)


# 2.- Do the same as the question one but this time use variables instead of 
# numbers.
var1 = 64
var2 = 32
sumOFVar = var1 + var2
print ("answer:" + str(sumOFVar))

# 3.- Make a program that prints a sentence that includes at least 3 variables.
sent1 = "Hi, I am Trushita\n"
sent2 = "I am 22 years old and "
sent3 = "I like to dance"
print(sent1+sent2+sent3)

# 4.- Given a sentence, assign the string to a variable then print the number of 
# characters in the sentence. 
# The sentence is "This is my first Python program."
sent4 = "This is my first Python program."
print(len(sent4))

# 5.- Given the resolution 1920 x 1080, make a program that prints a string with 
# the 10% over-scan value of those numbers. The printed string must be as 
# follows: "The 10% overscan of 1920 is <value 1>, and the 1080 is <value 2>"

res1 = 1920
res2 = 1080
res1percent = str((res1*10)/100)
res2percent = str((res2*10)/100)
solution = "The 10% overscan of 1920 is "+res1percent+", and the 1080 is "+res2percent
print(solution)



