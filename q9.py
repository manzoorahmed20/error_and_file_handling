with open("source.txt", "r") as source_file:
    data = source_file.read()

with open("destination.txt", "w") as destination_file:
    destination_file.write(data)

print("File copied successfully!")