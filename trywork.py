"""
 QUESTION: A loop that computes the sum of all numbers
            between 2 & 100 inclusive that are whole numbers
            of 5 & 7.
"""


def try_code():
    # create an empty list[] to store values.
    multiples_of_5 = []
    multiples_of_7 = []
    # loop through all values in range() and store in respected list.
    for i in range(2, 101):
        if i % 5 == 0:
            multiples_of_5.append(i)
            answer1 = sum(multiples_of_5)
        elif i % 7 == 0:
            multiples_of_7.append(i)
            answer2 = sum(multiples_of_7)

    print(f"sum of the two multiples, {answer1} + {answer2} = {answer1 + answer2}")
    print(f"multiples of 5 {multiples_of_5}")
    print(f"multiples of 7 {multiples_of_7}")


try_code()
