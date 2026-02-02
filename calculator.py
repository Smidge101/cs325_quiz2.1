user_input = input("Enter a mathematical expression to evaluate(+, -, *, /): ")

if '+' in user_input:
    user_input1 = int(input("Enter first number: "))
    user_input2 = int(input("Enter second number: "))
    result = user_input1 + user_input2
    print(f"The result is: {result}")

elif '-' in user_input:
    user_input1 = int(input("Enter first number: "))
    user_input2 = int(input("Enter second number: "))
    result = user_input1 - user_input2
    print(f"The result is: {result}")
