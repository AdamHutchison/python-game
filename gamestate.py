# State management class
class StateMachine(object):
    def __init__(self):
        self.player_location = 'Laser Weapon Armory'
        self.player_health = 100
        self.player_weapon = 'Buster Sword'
        self.enemy_location = 'Engine Room'
        self.enemy_health = 100
    
    def get_player_state(self):
        return {
            'location': self.player_location,
            'health': self.player_health,
            'weapon': self.player_weapon,
        }

    def get_enemy_state(self):
        return {
            'location': self.player_location,
            'health': self.player_health,
        }

    def set_health(self, character, new_health_stat):
        if character == 'player':
            self.player_health = new_health_stat
        elif character == 'enemy':
            self.enemy_health = new_health_stat
    
    def set_location(self, character, new_location):
        if character == 'player':
            self.player_location = new_location
        elif character == 'enemy':
            self.enemy_location = new_location