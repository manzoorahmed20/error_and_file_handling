try:
    number = 10 / 0
    print(number)
except ZeroDivisionError:
    print("An error occurred.")
finally:
    print("This will always execute.")