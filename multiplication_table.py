# version 0.2

for i in range(1, 10):
    for j in range(1, 10):
        x = i * j
        if x < 10 :
            print("  ", end="")
        else:
            print(" ", end="")
        print(x, end="|")
    print()
