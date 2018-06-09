with open("example.txt","r") as readfile:
    with open("example1.txt","w") as writefile:
        for line in readfile:
            writefile.write(line)
