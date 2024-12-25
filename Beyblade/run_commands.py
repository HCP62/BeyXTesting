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
    !win% = show win percentage
    !type = get all the options for a type of finish
    !type spin = get the percentage to score a spin finish
    !type over = get the percentage to score an over finish
    !type burst = get the percentage to score a burst finish
    !type x = get the percentage to score an extreme finish
    !q = quit'''
    print("Commands:", s)

def choose_option():
    input = input("Type the command: ")
    if input == "!start":
        match_runner.start_test()
    elif input == "!help":
        help()
    elif input == "!q":
        quit()