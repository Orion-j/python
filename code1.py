#  keyword argument, default keyword.
def introduction(name, company, country="Ghana"):
    intro = f"{name} from {country}, this is {company}."
    return intro.title()


welcome = introduction("joe", "microsoft")
print(welcome)
