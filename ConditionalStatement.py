motors = ["bmw", "audi", "toyota", "honda"]
for motor in motors:
    if motor == "bmw":
        print(motor.upper())
    else:
        print(motor.title())

if "bmw" in motors:
    print("some good cars we have")

if "hyundai" not in motors:
    print("Need to add Hyundai")

age = 20
if age > 20:
    price = 20
elif age < 20:
    price = 5
elif age:
    price = 20

print(f"pay ${price}")
