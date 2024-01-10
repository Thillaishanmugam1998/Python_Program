# Basic String Operations
# Concatenation
string1 = "Hello, "
string2 = "World!"
result_concatenation = string1 + string2
print(result_concatenation)

# Repetition
original_string = "abc"
result_repetition = original_string * 3
print(result_repetition)

# Slicing
substring = original_string[1:3]
print(substring)

# Length
length = len(original_string)
print(length)

# Iteration
for char in original_string:
    print(char)

# Membership
if "a" in original_string:
    print("a is present in the string")

# String formatting
formatted_string = "The value is: {}".format(42)
print(formatted_string)

# String interpolation (f-strings, available in Python 3.6+)
variable = 42
formatted_string = f"The value is: {variable}"
print(formatted_string)


# String Methods
# capitalize
capitalized_string = original_string.capitalize()
print(capitalized_string)

# lower
lowercase_string = original_string.lower()
print(lowercase_string)

# upper
uppercase_string = original_string.upper()
print(uppercase_string)

# title
title_case_string = "hello world".title()
print(title_case_string)

# swapcase
swapped_case_string = "Hello WoRLD".swapcase()
print(swapped_case_string)

# count
count_occurrences = original_string.count("a")
print(count_occurrences)

# find
index = original_string.find("b")
print(index)

# replace
replaced_string = original_string.replace("a", "x")
print(replaced_string)

# startswith
starts_with = original_string.startswith("ab")
print(starts_with)

# endswith
ends_with = original_string.endswith("bc")
print(ends_with)

# strip
whitespace_string = "   Hello, World!   "
stripped_string = whitespace_string.strip()
print(stripped_string)

# split
split_string = "one, two, three".split(", ")
print(split_string)

# join
words = ["Hello", "World", "!"]
joined_string = " ".join(words)
print(joined_string)

# isdigit
isdigit_result = original_string.isdigit()
print(isdigit_result)

# isalpha
isalpha_result = original_string.isalpha()
print(isalpha_result)

# isalnum
isalnum_result = original_string.isalnum()
print(isalnum_result)

# isspace
isspace_result = "   ".isspace()
print(isspace_result)


# Mutable String Operations using List
mutable_list = list(original_string)

# Changing a character at a specific index
mutable_list[1] = "x"
modified_string = "".join(mutable_list)
print(modified_string)

# Append to the end
mutable_list.append("d")
appended_string = "".join(mutable_list)
print(appended_string)

# Remove a character at a specific index
del mutable_list[0]
removed_string = "".join(mutable_list)
print(removed_string)

# Reverse the string
mutable_list.reverse()
reversed_string = "".join(mutable_list)
print(reversed_string)


# Custom String Operations
def remove_substring(input_string, substring_to_remove):
    # Check if the substring is present
    if substring_to_remove in input_string:
        # Replace the substring with an empty string
        return input_string.replace(substring_to_remove, '')
    else:
        # If substring is not present, return the original string
        return input_string

original_string_custom = "Hello, World! Hello, Python!"
substring_to_remove_custom = "Hello"

result_string_custom = remove_substring(original_string_custom, substring_to_remove_custom)
print(result_string_custom)
