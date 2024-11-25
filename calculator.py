

while True:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    operation = input("Enter the operation(+, -, *, /): " )

    if operation == "+":
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")

    elif operation == "-":
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")

    elif operation == "*":
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")

    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")

    play_again = input("Play again(yes/no)?") 

    if play_again.lower()!= "yes":
        break

print("Byeeeeee!")
        

