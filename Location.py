class Location:
    def __init__(self, game):
        self.game = game
        self.name = ''
        self.navigation = {}

    def handle_movement(self, command) -> bool:
        if command not in self.navigation:
            return False
        
        location = self.navigation[command]
        return self.game.change_location(location)

    def on_enter(self):
        return True
    
    def on_leave(self):
        return True
