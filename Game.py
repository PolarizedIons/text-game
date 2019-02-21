import DataLoader
from Location import Location

STARING_LOCATION = 'home'

class Game:
    def __init__(self):
        self._locations = {}
        self.location = None
    
    def setup(self):
        for name, data in DataLoader.load().items():
            loc = Location(self, data)
            self._locations[name] = loc
        
        self.location = self._locations[STARING_LOCATION]
    
    def run(self):
        while True:
            print("location: " + self.location.name)
            next_loc = self.location.handle_input(input('> '))
            if next_loc is False:
                print("nope try again")
            else:
                self.location = self._locations[next_loc]


def main():
    game = Game()
    game.setup()
    game.run()


if __name__ == "__main__":
    main()