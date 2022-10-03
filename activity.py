import random
response = input("press y to role or n to exit: ")

def dice(response):
    while response == 'y':
        no = random.randint(1,6)
        if(no == 1 and response == "y"):
            print("|   |")
            print("| * |")
            print("|   |")
            input("press y to role or n to exit: ")
        elif(no == 2 and response == "y"):
            print("|  *|")
            print("|   |")
            print("|*  |")
            input("press y to role or n to exit: ")
        elif(no == 3 and response == "y"):
            print("|  *|")
            print("| * |")
            print("|*  |")
            input("press y to role or n to exit: ")
        elif(no == 4 and response == "y"):
            print("|* *|")
            print("|   |")
            print("|* *|")
            input("press y to role or n to exit: ")
        elif(no == 5 and response == "y"):
            print("|* *|")
            print("| * |")
            print("|* *|")
            input("press y to role or n to exit: ")
        elif(no == 6 and response == "y"):
            print("|* *|")
            print("|* *|")
            print("|* *|")
            input("press y to role or n to exit: ")
        elif(response == "n"):
            print("Thanks for rolling the dice!")
dice(response)


