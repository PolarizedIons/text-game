class Location:
    def __init__(self, game, data):
        self.game = game
        self.name = data['name']
        self.navigation = data['navigation']
    
    def handle_input(self, command):
        if command in ['north', 'south', 'east', 'west', 'up', 'down']:
            return self.handle_movement(command)
        
        return False;
    
    def handle_movement(self, command):
        if command not in self.navigation:
            return False
        
        location = self.navigation[command];
        allowed = True;
        for condition in location['conditions']:
            print(condition)
            allowed = allowed and self.eval_condition(condition)


        return location['location'] if allowed else False
    
    def eval_condition(self, condition):
        if condition['type'] == 'item':
            return condition['value'] in self.game.items
        else:
            print("unknown condition type " + condition)
            return False