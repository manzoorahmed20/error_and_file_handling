try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print("Result:", result)

except (ZeroDivisionError, ValueError):
    print("Please enter a valid number other than zero.")