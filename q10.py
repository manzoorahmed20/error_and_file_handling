import os

if os.path.exists("test1.txt"):
    os.remove("test.txt")
    print("test.txt deleted successfully.")
else:
    print("test.txt does not exist.")