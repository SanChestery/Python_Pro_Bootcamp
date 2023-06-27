def greet():
    print("Hello")
    print("How do you do?")

def greet_with_name(name):
    print(f"Hello {name}")
    print("How do you do?")

def greet_with(name1, name2):
    print(f"Hello {name1}, Hello {name2}")

greet()
greet_with_name("Markus")
greet_with("Sandra", "Mirco")

