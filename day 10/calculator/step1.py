from art import logo



# add
def add(n1, n2):
    return n1 + n2

# subtract
def subtract(n1, n2):
    return n1 - n2
 
# Mutliply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    not_finished = True

    print(logo)

    num1 = float(input("What's the first number?: "))

    for op in operations:
        print(op)


    while not_finished:
    
        op_chosen = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

        function = operations[op_chosen]
        answer = function(num1, num2)

        print(f"{num1} {op_chosen} {num2} = {answer}")

        num1 = answer

        go_again = input(f"Type 'y' to continue calculating with {num1}, or type 'n' to start a new calculation.: ")

        if go_again == "n":
            not_finished = False
            calculator()

calculator()