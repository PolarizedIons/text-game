import Constants
from Location import Location


class Home(Location):
    def __init__(self, game):
        super().__init__(game)
        self.name = 'home'
        self.navigation = {
            Constants.DOWN: 'basement',
            Constants.SOUTH: 'woods',
        }
