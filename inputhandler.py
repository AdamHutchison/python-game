class InputHandler(object):
    def __init__(self, game):
        self.map = game.get('map').locations
        self.state_machine = game.get('state-machine')
    
    def get_next_location(self):
        current_location = self.map.get(self.state_machine.player_location)
        
        current_location.enter()
        current_location.display_input_options()

        user_input = input('> ')
        
        return current_location.location_options.get(user_input).get('location')