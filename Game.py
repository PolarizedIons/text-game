from Location import Location

class Game:
    def __init__(self):
        self._locations = {}
        self.location = None
        self.items = {}
    
    def setup(self):
        from data.Home import Home
        from data.Basement import Basement
        
        locs = [
            Home(self),
            Basement(self)
        ]

        for loc in locs:
            self._locations[loc.name] = loc
        
        self.location = locs[0]

    def change_location(self, new_loc):
        if not self.location.on_leave():
            return
        
        new_location = self._locations[new_loc]
        if not new_location.on_enter():
            return
        
        self.location = new_location

    def run(self):
        while True:
            print("current location: " + self.location.name)
            command = input('> ')

            if command in Location.DIRECTION:
                self.location.handle_movement(command)

def main():
    game = Game()
    game.setup()
    game.run()


if __name__ == "__main__":
    main()