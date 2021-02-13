import random
import os
import sys
import signal


def signal_handler(signal, frame):
    print("\nDetected CTRL-C. quitting")
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
os.system('cls' if os.name == 'nt' else 'clear')


def cow():
    print("""
             _n_n_
    .------`-|00/-'
   /  ##  ## (oo)
  / \## __   ./
 /   |//YY \|/
     |||   |||
     ^^^   ^^^
    """)


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
version = "Update 3 - 1.0.0"
low = 0
high = 1000
setLow = 0
setHigh = 1000
total = 0


def init(starts, stops, steps):
    global setLow
    global setHigh
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
    setLow = begin
    setHigh = stop
    number = random.randrange(int(begin), int(stop), int(step))
    return number


def start():
    global high
    global low
    global setHigh
    global setLow
    logo()
    print("Welcome to GUESS!\nYou can ether play of 3 preset difficulties, or practice!")
    print("\n\n\n[1]Normal Mode\n[2]Practice Mode\n[3]Random Mode\n\nType your choice below!")
    high = setHigh
    low = setLow
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
    elif choice == "3":
        print("You chose random mode... Pure chaos!")
        randommode()
    else:
        print("invalid input... quitting!")
        sys.exit(0)


def count():
    global total
    global mode
    if mode == "easy":
        total = 15
    elif mode == "medium":
        total = 10
    elif mode == "hard":
        total = 5
    elif mode == "practice":
        total = 9999999999


def randommode():
    global tries
    global generated
    global mode
    global total
    generated = init(random.randrange(0, 100, 1), random.randrange(0, 10000, 1), random.randrange(0, 100, 1))
    tries = random.randint(1, 100)
    total = tries
    main()


def difficulties():
    global tries
    global generated
    global mode
    logo()
    print("You chose mode 1, preset...\nChoose the level of difficulty you want:")
    print("\n\n\n[1]Hard - 1-1000, 5 tries\n[2]Normal - 1-1000, 10 tries\n[3]Easy - 1-1000, 15 tries\n\n")
    command = input("> ")
    generated = init(1, 1000, 1)
    if command == "1":
        tries = 5
        mode = "hard"
        print("chose hard difficulty... starting!")
        count()
        main()
    elif command == "2":
        tries = 10
        mode = "medium"
        print("chose medium difficulty... starting!")
        count()
        main()
    elif command == "3":
        tries = 15
        mode = "easy"
        print("chose easy difficulty... starting!")
        count()
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
    count()
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
    global tries
    global version
    global mode
    global low
    global high
    global setLow
    global setHigh
    global total
    global generated
    low = setLow
    high = setHigh
    while True:
        if tries > 0:
            command = cmd()
            if command == "help":
                print('type a number, if that number is the one your trying to guess, you win!\nIf not, you get higher/lower output.')
                print("type 'cls' to clear the screen")
                print("type 'help' to show this!")
                print("type 'exit' to quit!")
                print("type 'restart' to restart!")
                print("type 'info' to get info about your game!")
                print("try typing 'cow'?")
            if str.isdigit(command):
                if int(command) == int(generated):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("CONGRATS!")
                    tries = tries - 1
                    print("Tries used: " + str(int(total) - int(tries)))
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
            if command == "exit -y":
                sys.exit(0)
            if command == "restart":
                choice = input("Are you sure?[y/n]> ")
                if choice == "y":
                    start()
                else:
                    print("chose no...")
            if command == "restart -y":
                start()
            if command == "info":
                print("Version: " + version)
                print("Current Mode: " + mode)
                print("Number generated between " + str(setLow) + " and " + str(setHigh))
                print("Tries; left: " + str(tries) + ", used: " + str(total - tries) + ", total: " + str(total))
                print("known value; between " + str(low) + " and " + str(high))
            if command == "cow":
                cow()
        else:
            print("out of tries! better luck next time!")
            print("the number was: " + str(generated) + "\n\n")
            restart()


start()
