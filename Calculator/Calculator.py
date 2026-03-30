def calculator(num1,num2,op):
    if op == '+':
        return num1+num2
    elif op == '-':
        return num1-num2
    elif op == '*':
        return num1 * num2
    elif op == '**':
        return num1 ** num2
    elif op == '%':
        return num1 % num2
    elif op == '/':
        return num1/num2 if num2!=0 else "Error! Division by zero."
    else:
        return "Invalid operation!"

