# Seeing The World.
favoritePlaces = ["Paris", "Hawaii", "New York", "Rwanda"]
print(sorted(favoritePlaces))  # temporal sorting.
print(favoritePlaces)  # original list not changed even after the sorted() method.
print(sorted(favoritePlaces, reverse=True))  # temporary sorted list in reverse alphabetical order.
favoritePlaces.sort()
print(favoritePlaces)