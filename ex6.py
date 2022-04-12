# LP3THW Exercise 6

# int variable (despite the joke indicating it is binary)
types_of_people = 10

# set varibale to hold a format string to insert a different variable into the f string
x = f"There are {types_of_people} types of people."

# Set variables to hold strings and another format string to use those variables
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

# Print to two f strings with, of course, their embeded variables in place
print(x)
print(y)

# Print 2 new f strings with embeded f strings
print(f"I said: {x}")
print(f"I also said: '{y}'")

# variable to hold boolean value
hilarious = False

# Variable to hohld a new string that has the brackets for an f string (but note no "f")
joke_evaluation = "Isn't that joke so funny?! {}"

# Call the print function on joke evaluation and use the string format method to format a string and replace the placeholder (variable hilarious) with the specified value
print(joke_evaluation.format(hilarious))

# Two more variables holding strings
w = "This is the left side of..."
e = "a string with a right side."

# Basic string concatenation with built in operator function
print(w + e)
