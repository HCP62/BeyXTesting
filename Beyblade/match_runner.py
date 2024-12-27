from beyblade import Beyblade
from match import Match


'''
Function initializing the beyblades
'''
def initialize_beyblades():
    # initialization of the tested beyblade
    bey1_blade = input("Your blade: ")
    bey1_ratchet = input("Your ratchet: ")
    bey1_bit = input("Your bit: ")

    #initialization of the dummy beyblade
    bey2_blade = input("Opponent's blade: ")
    bey2_ratchet = input("Opponent's ratchet: ")
    bey2_bit = input("Opponent's bit: ")

    # bey_info = read_bey_info()
    # battles = read_battles("input2.txt")

    # bey1_blade = bey_info[0]
    # bey1_ratchet = bey_info[1]
    # bey1_bit = bey_info[2]

    # #initialization of the dummy beyblade
    # bey2_blade = bey_info[3]
    # bey2_ratchet = bey_info[4]
    # bey2_bit = bey_info[5]

    bey1 = Beyblade(bey1_blade, bey1_ratchet, bey1_bit)
    bey2 = Beyblade(bey2_blade, bey2_ratchet, bey2_bit)

    return [bey1, bey2]

'''
Function defining the start of the test session
'''
def start_test(bey1, bey2):
    matches = [] #list of matches containing unique match data

    # total battles should be near 30 to get the win rate to be accurate
    # reference: magic number 30
    total_battles = 0
    for i in range(10):
        print(total_battles)
        print(f"\nMatch {i + 1}")
        match = Match(bey1, bey2)
        match.battle()
        matches.append(match) #add match to the list after match is completed
        total_battles += match.get_total_battles()
    
    return matches
    

def win_command(bey1, bey2, matches):
    win_r = calculate_win_rate(bey1, matches)
    print(f"{bey1.__str__()} win rate against {bey2.__str__()}: {win_r}%")

'''
Function to calculate the win rate of the tested beyblade
'''
def calculate_win_rate(bey, matches):
    wins = bey.win_count()
    battles = sum(match.get_total_battles() for match in matches)
    return float(wins/battles) * 100

def get_win_by_type(matches, bey, wt):
    wins = bey.get_win_by_type(wt)
    total_wins = sum(match.get_total_battles() for match in matches)
    return float(wins/total_wins) * 100

# THE FUNCTIONS COMMENTED BELOW DO NOT WORK

# '''
# File input functions for easier debugging
# '''
# def read_bey_info():
#     file = open("input.txt","r")
#     bey_info = []
#     for line in file:
#         bey_info.append(line.strip())
    
#     return bey_info

# def read_battles(filename):
#     f = open(filename, "r")
#     arr = []
#     arr2 = []
#     for line in f:
#         if (line == " "):
#             arr2.append(arr)
#             arr = []
#             continue
#         else:
#             arr.append(line.split())
    
#     return arr2
