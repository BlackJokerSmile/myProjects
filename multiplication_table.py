# version 0.4
def interleaner():
     print("+" + "---+" * 11)

def multiply(x, y):
    if x == 0 :
        return y
    elif y == 0:
        return x
    else:
        return x * y

for c in range(0, 11):
    interleaner()
    print("|", end="")
    for l in range(0, 11):
        x = multiply(c, l)
        if x == 0:
            print("   |", end="")
            continue
        if x < 10 :
            print("  ", end="")
        elif x == 100:
            print("", end="")
        else:
            print(" ", end="")
        print(x, end="|")
    print()
interleaner()
