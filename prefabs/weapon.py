from ursina import *
from keybinds import keybinds


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
        self.can_attack = True

    def input(self, key):
        if key == keybinds['weapon_use']:
            self.attack()

    def attack(self):
        f = mouse.hovered_entity
        print('attacked')
        if f and self.can_attack:
            dist = distance(self.position, f.position)
            if dist < self.max_range:
                print(f'{f.name} is in range')
        self.can_attack = False
        invoke(Func(setattr, self, 'can_shoot', True), delay=self.delay)

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

    def input(self, key):
        if self.semi and self.mode == 'semi' and key == keybinds['weapon_use_semi']:
            self.attack()

    def update(self):
        if self.auto and self.mode == 'auto' and held_keys[keybinds['weapon_use_auto']]:
            self.attack()

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
            auto=False,
            semi=True,
            mode='semi',
            max_range=50,
            **kwargs
        )

class SprayGun(Gun):
    def __init__(self, **kwargs):
        super().__init__(
            auto=True,
            semi=False,
            mode='semi',
            max_range=40,
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

class P90(SprayGun):
    def __init__(self, **kwargs):
        super().__init__(
            name='P90',
            ammo=50,
            mag=50,
            reload=3.7,
            delay=.03,
            dmg=10,
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
            dmg=200,
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

class DEagle(HandGun):
    def __init__(self, **kwargs):
        super().__init__(
            name='DEagle',
            ammo=8,
            mag=8,
            reload=2,
            delay=.5,
            dmg=40,
            **kwargs
        )