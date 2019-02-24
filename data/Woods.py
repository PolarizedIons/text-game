import Constants
from Location import Location


class Woods(Location):
    def __init__(self, game):
        super().__init__(game)
        self.name = 'woods'
        self.navigation = {
            Constants.NORTH: 'home'
        }

    def on_enter(self):
        super().on_enter()
        print(f"There are {self.stats.enter_count * 4} mosquitoes flying around. You decide to go back inside")
        self.game.change_location('home')

