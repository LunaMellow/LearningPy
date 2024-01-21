"""

    Assignment Week 02
    -------------------
    Question 7a

    @brief   :  Python knowledge
    @author  :  Luna Sofie Bergh
    @date    :  21-01-2024

"""

# Importing sleep for small breaks
from time import sleep


# Little seperator
def linebreak():
    print("\n" + "-" * 60 + "")


def for_while_if():
    linebreak()
    print("\nTask 1: For, while and if")
    linebreak()
    sleep(2.5)

    # For loop
    print("\nLets try to count to a number of your choice")
    n = int(input(": "))

    for i in range(1, n + 1):
        print(i)
        sleep(0.25)

    # While loop
    linebreak()
    print("\nNow lets do it with a while loop, but count backwards")
    sleep(2.5)

    while n > 0:
        print(n)
        n -= 1
        sleep(0.25)

    # If statements
    linebreak()
    print("\nBut about if statements? Lets see what we can do with two numbers")

    print("\nType a number")
    num1 = int(input(": "))
    print("\nType another")
    num2 = int(input(": "))

    print("\nNow lets try seeing if your numbers are equal, greater or less")
    sleep(2.5)

    if num1 == num2:
        print("\nLooks like your numbers are the same tihi :-)")
    elif num1 > num2:
        print("\nLooks like your first number is greater than the other")
    else:
        print("\nLooks like your first number is less than the other")

    sleep(2.5)


def nestedLoops():
    linebreak()
    print("\nTask 2: Nested for loop")
    linebreak()
    sleep(2.5)

    # Nested loop
    print("\nSo nested loops are also a thing. Lets try making something cool")
    sleep(2.5)
    print("Lets give the nested loop the number 10. It might create a cool pattern ;-)\n")
    sleep(2.5)

    n = 10

    for i in range(0, n + 1):
        for j in range(0, n + 1):
            print(j + i, end=" ")
            sleep(0.05)
        print(" ")
        sleep(0.05)

    sleep(2.5)
    print("\nDo you see it? Looks like 2 triangles right?")
    sleep(2.5)


def simpleFunction():
    linebreak()
    print("\nTask 3: Functions")
    linebreak()
    sleep(2.5)

    print("\nSince this is a mathematics course, lets try some simple functions")

    def addition(x, y):
        return x + y

    def multiplication(x, y):
        return x * y

    def division(x, y):
        return x / y
        # // for whole number division

    def power(x, y):
        return x ** y

    print("\nType a number")
    num1 = int(input(": "))
    print("\nType another")
    num2 = int(input(": "))

    linebreak()

    print("\nNow lets call them with your numbers:"
          "\nAddition: " + str(addition(num1, num2)),
          "\nMultiplication: " + str(multiplication(num1, num2)),
          "\nDivision: " + str(division(num1, num2)),
          "\nPower: " + str(power(num1, num2)))


def longList():
    linebreak()
    print("\nTask 4: Long list of 10000 numbers")
    linebreak()
    sleep(2.5)

    print("\nLets add 10000 numbers to a list without using range")
    sleep(2.5)

    numList = []
    i = 0
    while i < 10000:
        numList.append(i)
        i += 1

    print("\nIn a few milliseconds, its done :-)")
    sleep(2.5)


def listToTuple():
    linebreak()
    print("\nTask 5: List to tuple")
    linebreak()
    sleep(2.5)

    print("\nLets add 100 numbers to a list same way as previous task")
    sleep(2.5)

    numList = []

    i = 0
    while i < 100:
        numList.append(i)
        i += 1

    print("\nList:")
    print(numList)
    print("\nTuple:")
    print(tuple(numList))


def runItAll():
    for_while_if()
    nestedLoops()
    simpleFunction()
    longList()
    listToTuple()


# Lets run it all :)
runItAll()
