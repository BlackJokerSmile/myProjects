#   version 0.9.1
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

def multy_table(columns_number, rows_number):
    print("Multyplication table {0} by {1}: ".format(columns_number, rows_number))
    for c in range(0, rows_number + 1):
        interlinear(columns_number)
        print("|", end="")
        for l in range(0, columns_number + 1):
            x = multiply(c, l)
            if x == 0:
                print("   |", end="")
                continue
            if x < 10 :
                print("  ", end="")
            elif x >= 100:
                print("", end="")
            else:
                print(" ", end="")
            print(x, end="|")
        print()
    interlinear(rows_number)

    # print example 10 to 10 table in initiation

multy_table(10, 10)

    # input request for printing x to y table

while True:
    multy_table(int(input("Write the columns number(x value): ")), int(input("Write the rows number(y value): ")))
