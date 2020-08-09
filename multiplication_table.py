# version 0.3
def interleaner():
     print("+" + "---+" * 9)

for i in range(1, 10):
    interleaner()
    print("|", end="")
    for j in range(1, 10):
        x = i * j
        if x < 10 :
            print("  ", end="")
        else:
            print(" ", end="")
        print(x, end="|")
    print()
interleaner()
