try:
    number = int(input("Enter a number: "))
    result = 10 / number

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print("No error occurred.")
    print("Result:", result)