text = "Musawir is SQA Engineer"
print(text.upper()) # Coverts to Uppercase
print(text.lower()) # Converts to Lowercase
print(len(text)) # Find lenth of a string
print(text[0]) # Access first letter
print(text[-1]) # Access last letter
print(text[0:6]) # Slicing first 6 characters

last_eight = text[-8:] # Slicing last 8 characters
print(last_eight)
"""
[-8:] → Starts 8 characters from the end, goes till the end.
text[:6]  # Gets characters from index 0 to 5 
"""

first_six = text[:6] # Another method of slicing first 6 characters
print(first_six)
"""
[:6] → Starts from index 0, goes up to 6 (excluding 6).
text[-6:]  # Gets characters from index -6 to the end
"""