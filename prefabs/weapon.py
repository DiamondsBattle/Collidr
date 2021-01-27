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

class SniperRifle(Gun):
    def __init__(self, **kwargs):
        super().__init__(
            auto=False,
            semi=True,
            mode='semi',
            dmg=90,
            max_range=400,
            **kwargs
        )

class AssaultRifle(Gun):
    def __init__(self, **kwargs):
        super().__init__(
            auto=True,
            semi=False,
            mode='auto',
            max_range=200,
            **kwargs
        )

class HandGun(Gun):
    def __init__(self, **kwargs):
        super().__init__(
            auto=True,
            semi=False,
            mode='semi',
            max_range=50,
            **kwargs
        )

class M4(AssaultRifle):
    def __init__(self, **kwargs):
        super().__init__(
            name='M4',
            ammo=30,
            mag=30,
            reload=3,
            delay=.07,
            dmg=33,
            **kwargs
        )

class AWP(SniperRifle):
    def __init__(self, **kwargs):
        super().__init__(
            name='AWP',
            ammo=5,
            mag=5,
            reload=2.5,
            delay=1,
            **kwargs
        )

class HuntingRifle(SniperRifle):
    def __init__(self, **kwargs):
        super().__init__(
            name='Hunting Rifle',
            ammo=10,
            mag=10,
            reload=6,
            delay=2,
            dmg=160,
            **kwargs
        )