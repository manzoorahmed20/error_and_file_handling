def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or older")
    else:
        print("Age is valid.")


try:
    age = int(input("Enter your age: "))
    check_age(age)

except ValueError as error:
    print(error)