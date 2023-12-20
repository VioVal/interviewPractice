def gridPrinter(size):
    noOfLines = ((size * 4) + 1)

    print("   ", end="")
    for i in range(noOfLines):
        print("-", end="")

    for i in range(size, 0, -1):
        print("\n" + str(i - 1) + "  |", end="")
        for j in range(size):
            print(" . |", end="")
        print("\n   ", end="")
        for j in range(noOfLines):
            print("-", end="")

    print("\n    ", end="")
    for i in range(size):
        print(" " + str(i) + "  ", end="")
    print("")

gridPrinter(10)