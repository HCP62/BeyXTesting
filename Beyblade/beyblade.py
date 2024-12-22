class Beyblade:
    '''
    Class defining the beyblade object
    '''
    def __init__(self, blade, ratchet, bit):
        self._blade = blade
        self._ratchet = ratchet
        self._bit = bit
        self._wins = []
        self._points = 0

    # getters
    def get_blade(self):
        return self._blade
    
    def get_ratchet(self):
        return self._ratchet
    
    def get_bit(self):
        return self._bit
    
    def get_wins(self):
        return self._wins
    
    def get_points(self):
        return self._points
    
    def add_win(self, victory):
        self._wins.append(victory)
    
    def add_points(self, points):
        self._points += points
    
    def win_count(self):
        return len(self._wins)

    def get_win_by_type(self, wt):
        count = 0
        for victory in self._wins:
            if (victory.get_type() == wt):
                count += 1
        return count
    
    def __eq__(self, other):
        return self._blade == other._blade and \
            self._ratchet == other._ratchet and \
            self._bit == other._bit
    
    '''
    Function to return the string representation of the beyblade
    '''
    def __str__(self):
        return f"{self._blade} {self._ratchet} {self._bit}"