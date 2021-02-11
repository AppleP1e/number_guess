import random
import os
import sys
os.system('cls' if os.name == 'nt' else 'clear')



def init():
    start = input("start number> ")
    stop = input("end number> ")
    step = input("step> ")
    number = random.randrange(int(start), int(stop), int(step))
    print("Random number was generated...")
    print("Start guessing! Type help if you would need help")
    return number


generated = init()


def restart():
    choice = input("play again?[y/n]> ")
    if choice == "y":
        os.system('cls' if os.name == 'nt' else 'clear')
        global generated
        generated = init()
    if choice != "y":
        print("replied no, quitting!")
        sys.exit(0)


def cmd():
    command = input("> ")
    return command


while True:
    command = cmd()
    if command == "help":
        os.system('cls' if os.name == 'nt' else 'clear')
        print('type a number, if that number is the one your trying to guess, you win!\nIf not, you get higher/lower output.')
        print("type 'cls' to clear the screen")
        print("type 'help' to show this!")
        print("type 'exit' to quit!")
    if str.isdigit(command):
        if int(command) == int(generated):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("CONGRATS!")
            restart()
        if int(command) > int(generated):
            print("higher!")
        if int(command) < int(generated):
            print("lower!")
    if command == "cls":
        os.system('cls' if os.name == 'nt' else 'clear')
    if command == "exit":
        sys.exit(0)
