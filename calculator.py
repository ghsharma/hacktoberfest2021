# calculator made by python.


first = input("enter the first number : ")
operator = input("enter the operator (=,-,*,/,%): ")
second = input("enter the second number : ")

first = int(first)
second = int(second)

if operator == "+":
    print("the sum of the numbers is : ",first + second)
elif operator == "-":
    print("the subtraction of the numbers is : ",first - second)
elif operator == "*":
    print("the multiplication of the numbers is : ",first * second)
elif operator == "/":
    print("the divison of the numbers is : ",first / second)
elif operator == "%":
    print("the remainder of the numbers is : ",first % second)
