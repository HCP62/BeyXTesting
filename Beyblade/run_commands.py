import match_runner
from beyblade import Beyblade
from match import Match
from victory import Victory

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
        elif command == "!type":
            get_type_options()
            choose_type(matches, beys[0])
        elif command == "!q":
            quit()

def get_type_options():
    s = '''
    !type spin = get the percentage to score a spin finish
    !type over = get the percentage to score an over finish
    !type burst = get the percentage to score a burst finish
    !type x = get the percentage to score an extreme finish
    '''
    print("Type options:", s)

def choose_type(match, bey):
    command = input("choose the type of finish: ")
    if command == "!type spin":
        print(f"{bey.__str__()} win rate for spin finishes: {match_runner.get_win_by_type(match, bey, 'spin')}%")
    elif command == "!type over": # not printing
        print(f"{bey.__str__()} win rate for over finishes: {match_runner.get_win_by_type(match, bey, 'over')}%")
    elif command == "!type burst": # not printing
        print(f"{bey.__str__()} win rate for burst finishes: {match_runner.get_win_by_type(match, bey, 'burst')}%")
    elif command == "!type x": # not printing
        print(f"{bey.__str__()} win rate for extreme finishes: {match_runner.get_win_by_type(match, bey, 'x')}%")

choose_option()