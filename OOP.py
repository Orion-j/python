class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        # method

    def More_info(self):
        manu_date = "01/10/2022"
        return f"{self.name} is sprayed {self.color}, manufactured in {manu_date}"


audi = Car("Audi", "Black")
honda = Car("Honda", "White")
print(audi.More_info())
print(honda.More_info())
