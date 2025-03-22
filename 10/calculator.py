import os
import sys
import art

print(art.logo)
first_number = int(input("What's the first number?: "))
nobreak = True

def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

while nobreak == True:
    print(f"+\n-\n*\n/")
    operator = str(input("Pick an Operation: "))
    second_number = int(input("What's the next number?: "))
    if operator in operations:
        function = operations[operator]
        first_number = function(first_number,second_number)
    else:
        print("Wrong Input!")

    print(f"Result = {first_number}")
    consent = input(f"Type 'y' to continue calculating with {first_number}, or type 'n' to start a new calculation : ")
    if consent == "n":
        os.system('cls' if os.name == 'nt' else 'clear')
        os.execv(sys.executable, ['python'] + sys.argv)