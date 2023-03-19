food ={}
ask= True
while ask:
    request = input("your food request: ")
    name = input("and your name? ")
    food[name] = request

    confirm = input("enter q to terminate ")
    if confirm == "q":
        ask = False

for request, name in food.items():
    print(food)