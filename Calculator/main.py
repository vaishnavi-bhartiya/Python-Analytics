from Calculator import calculator

history =[]

while True:
    op = input("enter the valid operations (+,-,/,*,%,**) or type 'exit' to end the operations or type 'history' to get historial value: ")

    if op == 'exit':
        print("End of operations. Thank You for using calculator.")
        break
    elif op == 'history':
        if history:
            print("Calculation History")
            for i,h in enumerate(history,start=1):
                print(f"{i}. {h}")
        else:
            print("No calculations yet!")
        continue

    try:
        num1 = float(input("Enter 1st number: "))
        num2 = float(input("Enter 2nd number: "))
    except ValueError:
        print("enter the valid number")
        continue

    result = calculator(num1,num2,op)
    output = f"result of {num1} {op} {num2} = {result}"
    print(output)
    history.append(output)
