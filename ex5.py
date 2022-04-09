my_name = 'Michael S. Dogan'
my_age = 50  # not a lie
my_height = 74  # inches
my_height_cm = my_height * 2.54
my_weight = 220  # lbs
my_weight_kg = my_weight * 0.453592
my_eyes = 'Hazel'
my_teeth = 'White'
my_hair = 'Brown'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"That is approximately {my_height_cm:.0f} centimeters.")
print(f"He's {my_weight} pounds heavy.")
print(f"That is approximately {my_weight_kg:.0f} kilograms.")
print("Actually, that is a little too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the soda.")

# this line is trick, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")
