try:
    file = open("non_existent_file.txt", "r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("File not found.")