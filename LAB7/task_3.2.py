
with open("example.txt", "w") as f:
    f.write("Hello, world!")
with open("data1.txt", "w") as f1:
    f1.write("First file content\n")
with open("data2.txt", "w") as f2:
    f2.write("Second file content\n")
print("Files written successfully")
try:
    with open("input.txt", "r") as infile:
        data = infile.readlines()
    with open("output.txt", "w") as output:
        for line in data:
            output.write(line.upper())
    print("Processing done")
except FileNotFoundError:
    print("input.txt not found - creating it with sample content")
    with open("input.txt", "w") as f:
        f.write("sample text\nfor demonstration\n")
    print("input.txt created, now processing...")
    with open("input.txt", "r") as infile:
        data = infile.readlines()
    with open("output.txt", "w") as output:
        for line in data:
            output.write(line.upper())
    print("Processing done")
try:
    with open("numbers.txt", "r") as f:
        lines = f.readlines()

    squares = []
    for n in lines:
        squares.append(int(n.strip())**2)

    with open("squares.txt", "w") as f:
        for sq in squares:
            f.write(str(sq) + "\n")
    print("Squares calculated and written to squares.txt")
except FileNotFoundError:
    print("numbers.txt not found - creating it with sample numbers")
    with open("numbers.txt", "w") as f:
        f.write("1\n2\n3\n4\n5\n")
    print("numbers.txt created, now processing...")
    with open("numbers.txt", "r") as f:
        lines = f.readlines()
    squares = []
    for n in lines:
        squares.append(int(n.strip())**2)
    with open("squares.txt", "w") as f:
        for sq in squares:
            f.write(str(sq) + "\n")
    print("Squares calculated and written to squares.txt")
try:
    with open("myfile.txt", "r") as f:
        data = f.read()
        print("Data read from myfile.txt:", data)
except FileNotFoundError:
    print("myfile.txt not found - creating it with sample content")
    with open("myfile.txt", "w") as f:
        f.write("Sample content for demonstration")
    print("myfile.txt created successfully")