import Constants
from Location import Location


class Basement(Location):
    def __init__(self, game):
        super().__init__(game)
        self.name = 'basement'
        self.navigation = {
            Constants.UP: 'home'
        }

    def on_leave(self):
        print("The ladder broke, you are now trapped")
        return False
