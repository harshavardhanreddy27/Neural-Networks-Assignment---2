# -*- coding: utf-8 -*-
"""Assignment - 2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1R9_LB9kEAnOgex2S6kpJXy8naoIhc-6A

### Question 1A:Takes two strings from the user: first_name, last_name. Pass these variables to fullname function that return fullname
"""

def fullname(first_name, last_name):
    return first_name + " " + last_name

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

full_name = fullname(first_name, last_name)
print("Your full name is:", full_name)

"""### Question1B Printing the Alternative characters in a word

"""

def string_alternative(full_name):
    return full_name[::2]

full_name = "Good Evening"
result = string_alternative(full_name)

print("Input string:", full_name)
print("Output string:", result)

"""### Question 2: Python program to find the wordcount in a file (input.txt) for each line and then print the output in Output.txt file"""

number_of_words = 0
with open('input.txt', 'r') as file:
    content = file.read()
    print(content)

number_of_words = 0
word_count = {}

with open('input.txt', 'r') as file:
    content = file.read()
    words = content.split()

    for word in words:
        word = word.strip().lower()
        word_count[word] = word_count.get(word, 0) + 1
        number_of_words += 1

print(f"Total Number of Words: {number_of_words}")

for word, count in word_count.items():
    print(f'{word}: {count}')

with open('output.txt', 'w') as output_file:
    print(f"Total Number of Words: {number_of_words}", file=output_file)

    for word, count in word_count.items():
        print(f'{word}: {count}', file=output_file)

"""### Question 3: Which reads heights (inches.) of customers into a list and convert these heights to centimeters in a separate list using:1) Nested Interactive loop. 2) List comprehensions"""

def convert_to_cm_nested(heights_inches):
    heights_cm = []
    for height in heights_inches:
        height_cm = height * 2.54
        heights_cm.append(round(height_cm, 2))
    return heights_cm

# 1) Using List Comprehensions
def convert_to_cm_list_comprehension(heights_inches):
    return [round(height * 2.54, 2) for height in heights_inches]
# 2) Using Nested Loop
def main():
    heights_inches = []

    input_str = input("Enter heights in inches separated by commas: ")

    try:
        heights_inches = [float(height) for height in input_str.split(',')]
    except ValueError:
        print("Invalid input. Please enter valid numbers separated by commas.")
        return


    heights_cm_nested = convert_to_cm_nested(heights_inches)


    heights_cm_list_comp = convert_to_cm_list_comprehension(heights_inches)

    print("\nHeights in Inches:", heights_inches)
    print("Heights in Centimeters (Using Nested Loop):", heights_cm_nested)
    print("Heights in Centimeters (Using List Comprehension):", heights_cm_list_comp)

if __name__ == "__main__":
    main()

