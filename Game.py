from typing import List, Dict

import Constants
from Location import Location


class Game:
    def __init__(self):
        self.running = True

        self._locations: Dict[str, Location] = {}
        self.location: Location = None
        self.items = {}
    
    def setup(self):
        from data.Home import Home
        from data.Basement import Basement
        
        locs: List[Location] = [
            Home(self),
            Basement(self)
        ]

        for loc in locs:
            self._locations[loc.name] = loc
        
        self.location = locs[0]

    def change_location(self, new_loc: str) -> bool:
        if not self.location.on_leave():
            return False
        
        new_location = self._locations[new_loc]
        if not new_location.on_enter():
            return False
        
        self.location = new_location
        return True

    def run(self):
        while self.running:
            print("current location: " + self.location.name)
            command = input('> ').lower()
            split_command = command.split(' ')

            if command in Constants.DIRECTION:
                if not self.location.handle_movement(command):
                    print("You cannot move that way")
            elif split_command[0] == 'move' and split_command[1] in Constants.DIRECTION:
                if not self.location.handle_movement(split_command[1]):
                    print("You cannot move that way")

            elif command == 'exit':
                self.running = False
            else:
                print("Unknown command!")


def main():
    game = Game()
    game.setup()
    game.run()


if __name__ == "__main__":
    main()
