programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
}

# Retrieving items from dictionary
print(programming_dictionary["Bug"])

# Adding new items to dictionary
programming_dictionary["new"] = "The new items"

print(programming_dictionary)

# Wipe a dictionary
# programming_dictionary = {}

# Editing an entry
programming_dictionary["Bug"] = "Some new info"

# Loop through dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
