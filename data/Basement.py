from Location import Location

class Basement(Location):
    def __init__(self, game):
        super().__init__(game)
        self.name = 'basement'
        self.navigation = {
            Location.UP: 'home'
        }
