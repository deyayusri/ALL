file_name = "x-file.txt"
fd = open(file_name,"a")
while True:
    line = input("Enter a line (or just press Enter to quit): ")
    if line:
        fd.write(line + "\n")
    else:
        break
fd.write("hello, world!")
fd.close()
