# assignment 03.
# (a) Pizza toppings.
print("BUY PIZZA WITH YOUR FAVORITE TOPPINGS.\nchoose your toppings or enter 'Quit' to terminate.")
toppings = ['Mushrooms', 'Gizzard', 'Vegetables', 'Beef']
print(','.join(toppings))
userPrompt = ""
while userPrompt != "quit":
    userPrompt = input("Choose your toppings: ").lower()
    print(f"{userPrompt} will be added to your pizza.")

# (b) movie tickets.
prompt = "Ticket pricing ranges with age."
print(f"MOVIE TICKET PRICING.\n{prompt}Choose your age to be priced.")
personAge = int(input("Your age: "))
congrat = " Enjoy the movie!"

if personAge < 3:
    print("Free entry, enjoy.")
elif 3 <= personAge <= 12:
    print(f"Pay $10.00 only for a ticket.{congrat}")
else:
    print(f"Pay $15.00 only for a ticket.{congrat}")

# (c)Infinity loop.
# x = 0
# while x < 5:
#   print("Infinity...")
