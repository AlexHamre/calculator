running = True
print("Type stop to stop loop")

while running:
    value1 = input("give number")
    try:
        value1 = float(value1)
    except:
        if value1 == "stop":
            running = False; print("Stopping loop")
        else:
            print("use a number next time")

    operator = input("give +,-,*,/")
    if operator == "stop":
        running = False; print("stopping loop")

    value2 = input("give another number")
    try:
        value2 = float(value2)
    except:
        if value2 == "stop":
            running = False; print("Stopping loop")
        else:
            print("use a number next time")

    if operator == "+":
        print(value1 + value2)

    elif operator == "-":
        print(value1 - value2)

    elif operator == "/":
        print(value1 / value2)

    elif operator == "*":
        print(value1 * value2)

    else:
        print("Error")
