with open("file.txt", "r+") as file:
    content = file.read()
    print("Original Content:", content)
    file.seek(0)
    file.write("Start")