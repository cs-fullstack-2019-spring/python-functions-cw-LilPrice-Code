def main():
    # prob1()
    # prob2()
    # prob3()
    prob4()


def prob1():
    x = 0
    while x <= number():
        print(x)
        x += 1


def prob3():
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    userReq = input("Do you want to add, subtract, multiply, or divide these numbers!: ")
    if userReq.lower() == "add":
        print(Add(num1, num2))

    elif userReq.lower() == "subtract":
        print(Sub(num1, num2))

    elif userReq.lower() == "multiply":
        print(Multi(num1, num2))

    elif userReq.lower() == "divide":
        print(Div(num1, num2))


def prob4():
    user1 = userInput1()
    user2 = userInput2()
    solution = Solution()

    if solution == "add":
        print(Add(user1, user2))

    elif solution == "subtract":
        print(Sub(user1, user2))

    elif solution == "multiply":
        print(Multi(user1, user2))

    elif solution == "divide":
        print(Div(user1, user2))

    else:
        print("ERROR")


def Add(a, b):
    return a + b


def Sub(a, b):
    return a - b


def Multi(a, b):
    return a * b


def Div(a, b):
    return a / b


def number():
    return 45


def userInput1():
    to = int(input("Enter a number: "))
    return to

def userInput2():
    po = int(input("Enter a number: "))
    return po


def Solution():
    fo = input("Do you want to add, subtract, multiply, or divide these numbers!: ")
    fo.lower()
    return fo


if __name__ == '__main__':
    main()
