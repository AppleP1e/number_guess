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


def init(starts, stops, steps):
    if starts is 0:
        begin = input("start number> ")
    else:
        begin = starts
    if stops is 0:
        stop = input("end number> ")
    else:
        stop = stops
    if steps is 0:
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
    else:
        print("invalid input... quitting!")
        sys.exit(0)


def difficulties():
    global tries
    global generated
    logo()
    print("You chose mode 1, preset...\nChoose the level of difficulty you want:")
    print("\n\n\n[1]Hard - 1-1000, 10 tries\n[2]Normal - 1-1000, 15 tries\n[3]Easy - 1-1000, 20 tries\n\n")
    command = input("> ")
    generated = init(1, 1000, 1)
    if command == "1":
        tries = 10
        print("chose hard difficulty... starting!")
        main()
    elif command == "2":
        tries = 15
        print("chose medium difficulty... starting!")
        main()
    elif command == "3":
        tries = 20
        print("chose easy difficulty... starting!")
        main()
    else:
        print("Invalid input... quitting!")
        sys.exit(0)


def practice():
    global tries
    global generated
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
        if tries > 0:
            command = cmd()
            if command == "help":
                print('type a number, if that number is the one your trying to guess, you win!\nIf not, you get higher/lower output.')
                print("type 'cls' to clear the screen")
                print("type 'help' to show this!")
                print("type 'exit' to quit!")
                print("type 'restart' to restart!")
            if str.isdigit(command):
                if int(command) == int(generated):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("CONGRATS!")
                    restart()
                    break
                if int(command) > int(generated):
                    print("lower!")
                    tries = tries - 1
                if int(command) < int(generated):
                    print("higher!")
                    tries = tries - 1
            if command == "cls":
                logo()
                os.system('cls' if os.name == 'nt' else 'clear')
            if command == "exit":
                sys.exit(0)
            if command == "restart":
                choice = input("Are you sure?[y/n]> ")
                if choice == "y":
                    start()
                else:
                    print("chose no...")
        else:
            print("out of tries! better luck next time!")
            restart()


start()
