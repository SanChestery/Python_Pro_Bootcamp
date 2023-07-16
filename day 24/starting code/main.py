with open("file.txt", mode="r") as file:
    contents = file.read()
    print(contents)

with open("new_file.txt", mode="a") as file:
    file.write("Appended text.")

with open("file.txt", mode="r") as file:
    contents = file.read()
    print(contents)