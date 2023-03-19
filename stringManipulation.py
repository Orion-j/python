"""
Name: Joe Orion
Date: 20/11/22
"""
letters = "YouCanDoItStayMotivated"

# using list comprehension
message = "".join([letter if letter.islower() else
                   # if letter is in lowercase nothing happens
                   f" {letter.upper()}" for letter in letters])[1:]
#  else  before any uppercase put a space in front.
# "[1:]"- only ignores the 'space' before the sentence(NB:we are dealing with a list)
print(message)
