# positional arguments.
# TODO: rewrite the function to take & display user input.

def myself(name, level, goal):
    print(f"{name} an {level} programmer aspire to work with {goal}")


myself("Joe", "intermediate", "Goldman Sachs")


# TODO: rewrite the function.

def useFunc():
    name = input("Name: ")
    level = input("Level of programming: ")
    goal = input("Dream company: ")
    # used  myself() function within this function.
    myself(name, level, goal)


useFunc()
