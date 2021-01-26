from ursina import *

class Weapon(Entity):
    def __init__(self,
                 name, dmg,
                 delay,
                 max_range,
                 **kwargs):
        super().__init__(**kwargs)

        self.name = name
        self.dmg = dmg
        self.max_range = max_range
        self.delay = delay

    def attack(self):
        f = mouse.hovered_entity
        print('ok')
        if distance(self, f) < 10:
            print('ok1')


class Gun(Weapon):
    def __init__(self,
                 ammo, mag,
                 auto, semi,
                 mode, reload,
                 **kwargs):
        super().__init__(**kwargs)

        self.ammo = ammo
        self.mag = mag
        self.auto = auto
        self.semi = semi
        self.mode = mode
        self.reload = reload

        self.can_shoot = True

        if self.ammo > self.mag:
            self.ammo = self.mag

        self.shoot = self.attack

    def input(self, key):
        if self.semi and self.mode == 'semi' and key == 'a':
            self.shoot()

    def reload(self):
        pass