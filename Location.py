class Location:
    def __init__(self, game):
        self.game = game
        self.name = ''
        self.navigation = {}

        self.stats = LocationStats()

    def handle_movement(self, command) -> bool:
        if command not in self.navigation:
            return False
        
        location = self.navigation[command]
        return self.game.change_location(location)

    def on_enter(self):
        self.stats.enter_count += 1
        return True
    
    def on_leave(self):
        self.stats.leave_count += 1
        return True


class LocationStats:
    def __init__(self):
        self.enter_count = 0
        self.leave_count = 0