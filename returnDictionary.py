# function to return a dictionary.
def full_profile(first_name, last_name, age=""):
    profile = {"firstname": first_name, "lastname": last_name}
    if age:
        profile["age"] = age
    return profile


icon = full_profile("Joe", "Orion")
icon2 = full_profile("Joe", "Orion", 25)
print(icon, "\n", icon2)


def full_profile2(firstname, lastname):
    profile = f"{firstname} {lastname}"
    return profile.title()


prompt = "Thank you for joining the train."
while True:
    print("enter your name:\nenter 'q' to quit.")

    first_name = input("firstname: ")
    if first_name == "q":
        print(prompt)
        break
    last_name = input("lastname: ")
    if last_name == "q":
        print(prompt)
        break

    introduce = full_profile2(first_name, last_name)
    print(f"you're welcome {introduce}")
