with open("example.txt","r") as file:
    i = 0
    for line in file:
        print("Iteration",i,":",line)
        i+=1
