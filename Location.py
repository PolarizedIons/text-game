

class Location:
    DOWN = 'down'
    UP = 'up'
    NORTH = 'north'
    SOUTH = 'south'
    EAST = 'east'
    WEST = 'west'

    DIRECTION = [DOWN, UP, NORTH, SOUTH, EAST, WEST]

    def __init__(self, game):
        self.game = game
        self.name = ''
        self.navigation = {}
    
    
    def handle_movement(self, command):
        if command not in self.navigation:
            return
        
        location = self.navigation[command]
        self.game.change_location(location)