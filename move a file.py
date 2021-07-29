import os

source ="copy.txt"
destination = " C:\\Users\\Home\\Desktop\\test.txt"

try:

    if os.path.exists(destination):
        print("There is already a file there")

    else:
        os.replace(source,destination)
        print(source+ "Was moved")

except FileNotFoundError:
    print(source +"was not found")

