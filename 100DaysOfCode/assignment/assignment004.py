#  assignment 4 code by:Joe Boadi.
def make_shirt(size, message):
    # message accepts text on shirt.
    return f'"{message}" shirt size {size}.'


#  (a) positional arguments.
print(make_shirt("XXL", "Focus And Make It"))
# keyword arguments.
ranSecondTime = make_shirt(size="XL", message="Who the Cap Fit...")
print(ranSecondTime)

print("\n")


# (b) modified function.
def make_shirt_modified(size="Large", message="I Love Python"):
    return f"{message} & I wear {size} size."


print(make_shirt_modified())
print(make_shirt_modified(size="Medium"))
print(make_shirt_modified(size="Very Large"))
print("\n")


# (c) Cities.
def describe_citty(city, country="Iceland"):
    return f"{city} is in {country}."


print(describe_citty("Reykjavik"))
print(describe_citty("Selfoss"))
print(describe_citty("Accra", "Ghana"))
