for i in range(10):
    line = ""
    for j in range(10):
        if (i+j) % 2 ==0:
            line += "* "
        else:
            line += "+ "
    print(line.strip())