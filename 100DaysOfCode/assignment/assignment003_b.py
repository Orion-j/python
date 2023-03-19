# assignment 03.
# (b) movie tickets.
prompt = "Ticket pricing ranges with age."
congrat = " Enjoy the movie!"
print(f"MOVIE TICKET PRICING.\n{prompt}Choose your age to be priced.")
personAge = int(input("Your age: "))
if personAge < 3:
    print("Free entry, enjoy.")
elif 3 <= personAge <= 12:
    print(f"Pay $10.00 only for a ticket.{congrat}")
else:
    print(f"Pay $15.00 only for a ticket.{congrat}")
