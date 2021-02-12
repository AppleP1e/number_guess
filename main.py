import random
import os
import sys
os.system('cls' if os.name == 'nt' else 'clear')


def logo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
:'######:::'##::::'##:'########::'######:::'######::
'##... ##:: ##:::: ##: ##.....::'##... ##:'##... ##:
 ##:::..::: ##:::: ##: ##::::::: ##:::..:: ##:::..::
 ##::'####: ##:::: ##: ######:::. ######::. ######::
 ##::: ##:: ##:::: ##: ##...:::::..... ##::..... ##:
 ##::: ##:: ##:::: ##: ##:::::::'##::: ##:'##::: ##:
. ######:::. #######:: ########:. ######::. ######::
:......:::::.......:::........:::......::::......:::
    """)


generated = 0
tries = 0
mode = "practice"
version = "update2"
low = 0
high = 1000


def init(starts, stops, steps):
    if starts == 0:
        begin = input("start number> ")
    else:
        begin = starts
    if stops == 0:
        stop = input("end number> ")
    else:
        stop = stops
    if steps == 0:
        step = input("step> ")
    else:
        step = steps
    number = random.randrange(int(begin), int(stop), int(step))
    return number


def start():
    logo()
    print("Welcome to GUESS!\nYou can ether play of 3 preset difficulties, or practice!")
    print("\n\n\n[1]Normal Mode\n[2]Practice Mode\n\nType your choice below!")
    choice = input("> ")
    if choice == "1":
        difficulties()
    elif choice == "2":
        practice()
    elif choice == "exit":
        choice = input("Are you sure?[y/n]> ")
        if choice == "y":
            sys.exit(0)
        else:
            start()
    else:
        print("invalid input... quitting!")
        sys.exit(0)


def difficulties():
    global tries
    global generated
    global mode
    logo()
    print("You chose mode 1, preset...\nChoose the level of difficulty you want:")
    print("\n\n\n[1]Hard - 1-1000, 10 tries\n[2]Normal - 1-1000, 15 tries\n[3]Easy - 1-1000, 20 tries\n\n")
    command = input("> ")
    generated = init(1, 1000, 1)
    if command == "1":
        tries = 10
        mode = "hard"
        print("chose hard difficulty... starting!")
        main()
    elif command == "2":
        tries = 15
        mode = "medium"
        print("chose medium difficulty... starting!")
        main()
    elif command == "3":
        tries = 20
        mode = "easy"
        print("chose easy difficulty... starting!")
        main()
    elif command == "back":
        start()
    elif command == "exit":
        choice = input("Are you sure?[y/n]> ")
        if choice == "y":
            sys.exit(0)
        else:
            difficulties()
    else:
        print("Invalid input... quitting!")
        sys.exit(0)


def practice():
    global tries
    global mode
    global generated
    mode = "practice"
    logo()
    print("you chose practice mode! you have infinite tries, and you can set whatever values you want!")
    generated = init(0, 0, 0)
    tries = 9999999999
    main()


def restart():
    choice = input("play again?[y/n]> ")
    if choice == "y":
        start()
    else:
        print("replied no, quitting!")
        sys.exit(0)


def cmd():
    command = input("> ")
    return command


def main():
    while True:
        global tries
        global version
        global mode
        global low
        global high
        if tries > 0:
            command = cmd()
            if command == "help":
                print('type a number, if that number is the one your trying to guess, you win!\nIf not, you get higher/lower output.')
                print("type 'cls' to clear the screen")
                print("type 'help' to show this!")
                print("type 'exit' to quit!")
                print("type 'restart' to restart!")
                print("type 'info' to get info about your game!")
            if str.isdigit(command):
                if int(command) == int(generated):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("CONGRATS!")
                    restart()
                    break
                if int(command) > int(generated):
                    print("lower!")
                    if int(command) < int(high):
                        high = int(command)
                    tries = tries - 1
                if int(command) < int(generated):
                    print("higher!")
                    if int(command) > int(low):
                        low = int(command)
                    tries = tries - 1
            if command == "cls":
                logo()
            if command == "exit":
                choice = input("Are you sure?[y/n]> ")
                if choice == "y":
                    sys.exit(0)
                else:
                    print("chose no...")
            if command == "restart":
                choice = input("Are you sure?[y/n]> ")
                if choice == "y":
                    start()
                else:
                    print("chose no...")
            if command == "info":
                print("Version: " + version)
                print("Current Mode: " + mode)
                total = 0
                if mode == "easy":
                    total = 20
                elif mode == "medium":
                    total = 15
                elif mode == "hard":
                    total = 10
                elif total == "practice":
                    total = 9999999999
                print("Tries; left: " + str(tries) + " used: " + str(total - tries) + " total: " + str(total))
                print("known value; between " + str(low) + " and " + str(high))
        else:
            print("out of tries! better luck next time!")
            restart()


start()
