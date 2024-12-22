from victory import Victory


class Match:
    '''
    Class defining the match object
    '''
    def __init__(self, bey1, bey2):
        self._total_battles = 0
        self._bey1 = bey1
        self._bey2 = bey2
        self._bey1_points = 0
        self._bey2_points = 0
        self._winner = None

    '''
    Function to get the total number of battles in the match
    '''
    def get_total_battles(self):
        return self._total_battles

    '''
    Function to get the tested beyblade
    '''
    def get_bey1(self):
        return self._bey1
    
    '''
    Function to get the dummy beyblade
    '''
    def get_bey2(self):
        return self._bey2
    
    '''
    Function to get the winner of the match
    '''
    def get_winner(self):
        return self._winner

    '''
    Function to determine the winner of the match
    '''
    def winner(self):
        if (self._bey1_points >= 4):
            self._winner = self._bey1
        elif (self._bey2_points >= 4):
            self._winner = self._bey2
    
    '''
    Function to add points to the beyblade based on the victory type
    using the victory object
    '''
    def scoring(self, bey, wt):
        bey_victory = Victory(bey, wt)
        bey_victory.add(wt)
        bey.add_win(bey_victory)

        points = 0
        wt = wt.lower()
        if wt == "burst" or wt == "over":
            points = 2
        elif wt == "spin":
            points = 1
        elif wt == "x" or wt == "extreme":
            points = 3

        if bey == self._bey1:
            self._bey1_points += points
        elif bey == self._bey2:
            self._bey2_points += points
        
        bey.add_points(points) # add points to the beyblade object

    '''
    Function that faciliates each battle in the match
    '''
    def battle(self):
        while self._winner is None:
            print(f"Battle {self._total_battles + 1}")
            self._total_battles += 1
            choice = input("Type 1 for you, 2 for your opponent\n")
            wt = input("What kind of victory? ")
            if (choice == "1"): 
                self.scoring(self._bey1, wt)
            elif (choice == "2"):
                self.scoring(self._bey2, wt)
            self.winner()
        print(f"{self._winner} wins the battle\n\n")
        return self._winner