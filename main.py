num1 = int(input("Enter your num --> "))
num2 = int(input("Enter your num --> "))
try:
    if num2 == 0:
        raise ZeroDivisionError("Second num cant be zero")
    print(num1/num2)
except:
    print("Invalid input")

def showDivision(num1,num2):
    print(num1/num2)

try:
    if num2 == 0:
        raise ZeroDivisionError("Second num cant be zero")
    showDivision(num1,num2)
except:
    print("Invalid input")

def showDivisionV2(num1,num2):
    try:
        if num2 == 0:
            raise ZeroDivisionError("Second num cant be zero")
        print(num1/num2)
    except:
        print("Invalid input")

showDivisionV2(num1,num2)

my_str = input("Enter your num --> ")
try:
    my_str = int(my_str)
except:
    ("String must be a number")
print(type(my_str))

def showRep(string):
    string = int(string)
    print(type(string))

try:
    showRep(my_str)
except:
    ("String must be a number")

def showRepV2(string):
    try:
        my_str = int(my_str)
    except:
        ("String must be a number")
    print(type(string))

showRepV2(my_str)