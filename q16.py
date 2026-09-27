student = {"name": "Faiq"}

try:
    print(student["age"])
except KeyError:
    print("The key 'age' does not exist.")