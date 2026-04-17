# import os

# script_dir = os.path.dirname(os.path.abspath(__file__))
# file_path = os.path.join(script_dir, "test.txt")

# f = open(file_path, "r")

# content = f.read()
# print(content)
# f.close()

f = open("test1.txt", "w")
f.write("This is a test file")
f.close() 