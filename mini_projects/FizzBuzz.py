"""  a simple program with application from
modulos and if-else statement function. """


def fix_bug(value):
    if value % 3 == 0 and value % 5 == 0:
        # returns if number is divisible by both 3 & 5.
        return "Fix Bug"
    elif value % 5 == 0:
        return "Fix"
    elif value % 3 == 0:
        return "Bug"
    #  returns the value not satisfying the conditions above.
    return value


print(fix_bug(25))  # display the result after returning.
