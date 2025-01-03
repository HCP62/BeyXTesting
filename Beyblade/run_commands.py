import match_runner

def command_set():
    print("Welcome to BeyX Tester")
    print("Type '!start' to start a test session")
    print("Type '!help' to see all the commands")
    print("Type '!q'  or '!quit' to exit")

def help():
    s = '''
    !start = start a test session
    !help = show all the commands
    !wr = show win percentage
    !type = get all the options for a type of finish
    !type spin = get the percentage to score a spin finish
    !type over = get the percentage to score an over finish
    !type burst = get the percentage to score a burst finish
    !type x = get the percentage to score an extreme finish
    !q = quit'''
    print("Commands:", s)

def choose_option():
    matches = []
    beys = []
    command = ""
    while command != "!q":
        command = input()
        if command == "!start":
            beys = match_runner.initialize_beyblades()
            matches = match_runner.start_test(beys[0], beys[1])
        elif command == "!help":
            help()
        elif command == "!wr":
            match_runner.win_command(beys[0], beys[1], matches)
        elif command.startswith("!type "):
            type_finish = command.split(" ")[1]
            if type_finish in ["spin", "over", "burst", "x"]:
                print(f"{beys[0].__str__()} win rate for {type_finish} finishes: {match_runner.get_win_by_type(matches, beys[0], type_finish)}%")
            else:
                get_type_options()
        elif command == "!q":
            quit()

def get_type_options():
    s = '''
    !type spin = get the percentage to score a spin finish
    !type over = get the percentage to score an over finish
    !type burst = get the percentage to score a burst finish
    !type x = get the percentage to score an extreme finish
    !back = return to main menu
    '''
    print("Type options:", s)