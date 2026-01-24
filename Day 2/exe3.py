try:
    num = int(input("Enter number: "))
    print(10 / num)
except ValueError:
    print("Invalid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
