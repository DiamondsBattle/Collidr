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
        # Disgusting line of code v
        if f and distance(self.position, f.position) <= self.max_range and f.takes_damage and f.life >= 0:
            f.life -= self.dmg
        self.can_attack = False
        invoke(Func(setattr, self, 'can_attack', True), delay=self.delay)

class Gun(Weapon):
    def __init__(self,
                 ammo, mag,
                 auto, semi,
                 mode, rld_time,
                 **kwargs):
        super().__init__(**kwargs)

        self.ammo = ammo
        self.mag = mag
        self.auto = auto
        self.semi = semi
        self.mode = mode
        self.rld_time = rld_time

        if self.ammo > self.mag:
            self.ammo = self.mag

        self.ammo_counter = Text(
            text=f'{self.ammo}/{self.mag}',
            scale=1,
            position=Vec3(),
        )

    def input(self, key):
        if self.semi and self.mode == 'semi' and key == keybinds['weapon_use_semi'] and self.can_attack:
            self.shoot()

    def update(self):
        if self.auto and self.mode == 'auto' and held_keys[keybinds['weapon_use_auto']] and self.can_attack:
            self.shoot()

        self.ammo_counter.text = f'{self.ammo}/{self.mag}'

    def renderBullet(self, to):
        bullet = Entity(
            model='cube',
            collider='box',
            scale=.3,
        )
        bullet.animate('position', Vec3(to.position), duration=distance(bullet, to))

    def shoot(self):
        self.ammo -= 1 if self.ammo > 0 else 0

        f = mouse.hovered_entity
        if f:
            if distance(self.position, f.position) <= self.max_range:
                print(f'shoot to {f.name}')

        if self.ammo <= 0:
            self.reload()

        self.can_attack = False
        invoke(Func(setattr, self, 'can_attack', True), delay=self.delay)

    def reload(self):
        self.can_attack = False
        invoke(Func(setattr, self, 'ammo', self.mag), delay=self.rld_time)
        invoke(Func(setattr, self, 'can_attack', True), delay=self.rld_time)

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
            rld_time=3,
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
            rld_time=3.7,
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
            rld_time=2.5,
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
            rld_time=6,
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
            rld_time=2,
            delay=.5,
            dmg=40,
            **kwargs
        )