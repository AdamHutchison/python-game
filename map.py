import locations

class Map(object):
    def __init__(self):
        self.locations = {
            'Laser Weapon Armory': locations.LaserWeaponArmory(),
            'Engine Room': locations.EngineRoom(),
            'Escape Pod': locations.EscapePod(),
        }
