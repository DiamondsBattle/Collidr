from ursina import *

class Weapon(Entity):
    def __init__(self,
                 name, dmg,
                 max_range,
                 **kwargs):
        super().__init__(**kwargs)

        self.name = name
        self.dmg = dmg
        self.max_range = max_range

    def attack(self):
        f = mouse.hovered
        if distance(self, f) < 10:
            print('ok')


class Gun(Weapon):
    def __init__(self,
                 ammo, mag,
                 auto, semi,
                 mode, reload,
                 **kwargs):
        super().__init__(**kwargs)

        self.ammo = ammo
        self.mag = mag
        self.shoot_delay = shoot_delay
        self.name = name
        self.auto = auto
        self.semi = semi
        self.mode = mode
        self.dmg = dmg
        self.reload = reload
        self.max_range = max_range

        self.can_shoot = True

        if self.ammo > self.mag:
            self.ammo = self.mag

        self.attack = self.shoot


    def reload(self):
        pass

    def shoot(self):
        self.can_shoot = False
