#   version 0.9.0
#   Made by BlackJokerSmile
# github link:  https://github.com/BlackJokerSmile
# gitnub repo: https://github.com/BlackJokerSmile/myProjects

    # prints interlinear decoration with lenght specified in multy_table() argument input

def interlinear(line_lenght):
     print("+" + "---+" * (line_lenght + 1))


    # returns (nonzero value --> with one zero or both nonzero argument) and (zero value --> with two zero arguments)

def multiply(x, y):
    if x == 0 :
        return y
    elif y == 0:
        return x
    else:
        return x * y

    # print the x to y multiplication table specified by arguments input

def multy_table(column_lenght, line_lenght):
    print("Multyplication table {0} by {1}: ".format(column_lenght, line_lenght))
    for c in range(0, column_lenght + 1):
        interlinear(line_lenght)
        print("|", end="")
        for l in range(0, line_lenght + 1):
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
    interlinear(line_lenght)

    # print example 10 to 10 table in initiation

multy_table(10, 10)

    # input request for printing x to y table

multy_table(int(input("Write the columns number(x value): ")), int(input("Write the lines number(y value): ")))
