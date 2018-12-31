# Super classes
class Location(object):
    def __init__(self):
        self.name = None
        self.location_options = None

    def display_input_options(self):
     print("====== Here are your options, choose wisely ======")
     for option, option_values in self.location_options.items():
         print(f"{option}. {option_values.get('message')}")

# Classes inheriting from Location
class EscapePod(Location):
    def __init__(self):
        self.name = 'Escape Pod'
        self.location_options = {
            "1" : {'message': 'Enter the Laser Weapon Armory', 'location' : 'Laser Weapon Armory'},
            "2" : {'message': 'Enter the Engine Room', 'location' : 'Engine Room'}
        }
    
    def enter(self):
        print(f"""
        you are now in the {self.name}
        """)

class EngineRoom(Location):
    def __init__(self):
        self.name = 'Engine Room'
        self.location_options = {
            "1" : {'message': 'Enter the Laser Weapon Armory', 'location' : 'Laser Weapon Armory'},
            "2" : {'message': 'Enter the Escape Pod', 'location' : 'Escape Pod'}
        }
    
    def enter(self):
        print(f"""
        you are now in the {self.name}
        """)

class LaserWeaponArmory(Location):
    def __init__(self):
        self.name = 'Laser Weapon Armory'
        self.location_options = {
            "1" : {'message': 'Enter the Engine Room', 'location' : 'Engine Room'},
            "2" : {'message': 'Enter the Escape Pod', 'location' : 'Escape Pod'}
        }
    
    def enter(self):
        print(f"""
        you are now in the {self.name}
        """)
