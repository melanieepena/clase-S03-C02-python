filename = "nota_10.txt"
# filename = "code_10.exe"

if "nota" in filename:
    print(filename)
elif "nota" not in filename:
    print(f"{filename} goes in the trash")

options = "012345"

if "*" in options:
    print("found it")
else:
    print("not found it")
