class Victory:
    '''
    Class defining the victory object
    '''
    def __init__(self, bey, wt):
        self._bey = bey
        self._type = wt
        self._points = 0

    def get_bey(self):
        return self._bey
    
    def get_type(self):
        return self._type
    
    def get_spins(self):
        return self._spins
    
    def get_bursts(self):
        return self._bursts
    
    def get_over(self):
        return self._over
    
    def get_x(self):
        return self._x
    
    '''
    Function to return the string representation of the victory
    '''
    def __str__(self):
        return (self._bey.__str__() + " " + self._type)

    '''
    Function to add points to the beyblade based on the victory type
    '''
    def add(self, wt):
        if (wt == "spin"):
            self._bey.add_points(1)
            self._points = 1
        elif (wt == "burst"):
            self._bey.add_points(2)
            self._points = 2
        elif (wt == "over"):
            self._bey.add_points(2)
            self._points = 2
        elif (wt == "x" or wt == "X" or wt == "extreme"):
            self._bey.add_points(3)
            self._points = 3
