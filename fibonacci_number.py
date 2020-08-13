#   version 0.1
#   Made by BlackJokerSmile
# github link:  https://github.com/BlackJokerSmile
# gitnub repo:  https://github.com/BlackJokerSmile/myProjects

a, b = 0, 1

def Fibonacci(number_of_operations):
    try:
        number_of_operations = int(number_of_operations)
        if number_of_operations > 0:
            global a
            global b
            for i in range(0 ,number_of_operations):
                print(a)
                a, b = b, a+b
            return a
        else:
            print("Please enter the integer number bigger then 0")
    except(TypeError, ValueError):
        print("Please enter the integer bigger then 0")

while True:
    Fibonacci(input("Enter the number of operations: "))
