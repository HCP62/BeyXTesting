from beyblade import Beyblade
from victory import Victory
from match import Match


'''
Function defining the start of the test session
'''
def start_test():
    #initialization of the tested beyblade
    bey1_blade = input("Your blade: ")
    bey1_ratchet = input("Your ratchet: ")
    bey1_bit = input("Your bit: ")

    print("\n")

    #initialization of the dummy beyblade
    bey2_blade = input("Opponent's blade: ")
    bey2_ratchet = input("Opponent's ratchet: ")
    bey2_bit = input("Opponent's bit: ")

    bey1 = Beyblade(bey1_blade, bey1_ratchet, bey1_bit)
    bey2 = Beyblade(bey2_blade, bey2_ratchet, bey2_bit)

    matches = [] #list of matches containing unique match data

    # total battles should be near 30 to get the win rate to be accurate
    # reference: magic number 30
    total_battles = 0
    for i in range(10):
        print(f"\nMatch {i + 1}")
        match = Match(bey1, bey2)
        match.battle()
        matches.append(match) #add match to the list after match is completed
        total_battles += match.get_total_battles()
    
    win_r = calculate_win_rate(bey1, matches)
    print(f"{bey1._str_()} win rate against {bey2._str_()}: {win_r}%")

'''
Function to calculate the win rate of the tested beyblade
'''
def calculate_win_rate(bey, match):
    wins = bey.win_count()
    battles = match.get_total_battles()
    return float(wins/battles) * 100

def main():
    start_test()

main()
