"""Python for Visual Effects.

Assignment #2 - Functions and Conditionals
Answer the following questions.

Remember to be precise with the answer. The code will be tested using a pytest 
# 1.- Complete the body of the format_name function. 
# This function receives first_name and last_name, then prints a formatted 
# string of "Name: last_name, first_name" if both names are not blank, or 
# "Name: <first_name or last_name>" with just one of the names, if the other one
# is blank, and nothing if both are blank.
# Add the docstring in the function.
"""
def format_name(first_name, last_name):
    result = ""
    if(first_name != "" and last_name != ""):
        result = "Name: " + last_name + ", "  + first_name
        return result
    elif(first_name == "" and last_name != ""):
        result = "Name: "+ last_name
        return result

    elif(first_name != "" and last_name == ""):
        result = "Name: "+ first_name
        return result
    else:
        result = ""
        return result

# 2.- Flesh out the body of the get_seconds function so that it RETURNS the
# total amount of seconds given the hours, minutes and seconds function
# arguments. Remember that there are 3600 seconds in an hour and 60 seconds in
# a minute. Must return an integer.
# Add the docstring in the function.
def get_seconds(hours, minutes, seconds):
    hoursToSec = (hours*60)*60
    minutesToSec = minutes*60
    result = hoursToSec+minutesToSec+seconds
    return result

# 3.- Complete the function by filling in the missing parts. 
# The color_translator function receives the name of a color, then prints its 
# hexadecimal value. Currently, it only supports the three additive primary 
# colors (red, green, blue), so it returns "unknown" for all other colors.
# Add the docstring in the function.
def color_translator(color):
    if color == "red":
        hex_color = "#ff0000"
    elif color == "green":
        hex_color = "#00ff00"
    elif color == "blue":
        hex_color = "#0000ff"
    else:
        hex_color = "unknown"
    return hex_color

# 4.- In this scenerio, we have a directory with 5 files in it. Each file has a
# a different size: 2048, 4357, 97658, 125 and 8. calculate the average file
# file size by having Python add all the values for you, and then set the amount 
# variable to the amount of files. Finally, RETURN a message saying:
# "The average size is: X" followed by the resulting number. Remember to use the
# str() function to convert the number into a string.
# Use those values directly inside the function, no need to add them as
# arguments.
# Add the docstring in the function.
def average_size(mydict):
    amount = len(mydict.keys())
    values = mydict.values()
    sumofall = 0
    for val in values:
        sumofall = int(sumofall) + int(val)
        
    return sumofall/amount

mydict = {'size1': 2048, 'size2':4357, 'size3':97658, 'size4':125 , 'size5':8}

average_size(mydict)

# 5.- Complete the following function. It must convert from Celsius to 
# Fahrenheit degrees. The value returned must be float value.
# Add the docstring in the function. Must return a float.
def convert_degrees(celsius_degree):
    Fahrenheit = (celsius_degree * 1.8) + 32 
    return Fahrenheit