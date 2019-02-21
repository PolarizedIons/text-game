class Location:
    def __init__(self, game, data):
        self.game = game
        self.name = data['name']
        self.navigation = data['navigation']
    
    def handle_input(self, option):
        if option not in self.navigation:
            return False
        
        return self.navigation[option]['location']