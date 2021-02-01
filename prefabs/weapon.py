from ursina import *
from keybinds import keybinds


class Weapon(Entity):
    def __init__(self,
                 name, dmg,
                 delay,
                 max_range,
                 **kwargs):

        self.name = name
        self.dmg = dmg
        self.max_range = max_range
        self.delay = delay
        self.can_attack = True

        super().__init__(**kwargs)

    def input(self, key):
        if key == keybinds['weapon_use']:
            self.attack()

    def attack(self):
        f = mouse.hovered_entity
        if f and\
                distance(self.position, f.position) <= self.max_range and\
                f.takes_damage and\
                f.life >= 0:
            f.life -= self.dmg
        self.can_attack = False
        invoke(Func(setattr, self, 'can_attack', True), delay=self.delay)

class Gun(Weapon):
    def __init__(self,
                 mag, mag_size,
                 auto, semi,
                 mode, rld_time,
                 ammo,
                 **kwargs):

        self.mag = mag
        self.mag_size = mag_size
        if self.mag > self.mag_size:
            self.mag = self.mag_size

        self.ammo = ammo

        self.auto = auto
        self.semi = semi
        self.mode = mode
        self.rld_time = rld_time

        self.ammo_counter = Text(
            text=f'{self.mag}/{self.ammo}',
            scale=1,
            position=Vec3(),
        )

        super().__init__(**kwargs)

    def input(self, key):
        if self.semi and\
                self.mode == 'semi' and\
                key == keybinds['weapon_use_semi'] and\
                self.can_attack and\
                self.mag >= 1:
            self.shoot()

        if key == keybinds['weapon_rld'] and self.ammo > 0:
            invoke(self.reload, delay=self.rld_time)

    def update(self):
        if self.auto and\
                self.mode == 'auto' and\
                held_keys[keybinds['weapon_use_auto']] and\
                self.can_attack and\
                self.mag >= 1:
            self.shoot()

        self.ammo_counter.text = f'{self.mag}/{self.ammo}'

        if self.parent.name == 'controller':
            self.rotation_x = self.parent.rotation_x

    def renderBullet(self, to):
        bullet = Entity(
            model='cube',
            collider='box',
            scale=.3,
        )
        bullet.animate('position', Vec3(to.position), duration=distance(bullet, to))

    def shoot(self):
        self.can_attack = False
        invoke(Func(setattr, self, 'can_attack', True), delay=self.delay)

        self.mag -= 1

        f = mouse.hovered_entity
        if f:
            if distance(self.position, f.position) <= self.max_range:
                print(f'shoot to {f.name}')

        if self.mag <= 0 and self.ammo > 0:
            self.can_attack = False
            invoke(self.reload, delay=self.rld_time)

    def reload(self):
        if self.ammo > 0:
            if self.ammo < self.mag_size:
                dif = self.mag_size - self.mag
                if self.ammo > dif:
                    self.mag += dif
                    self.ammo -= dif
                else:
                    self.mag += self.ammo
                    self.ammo = 0

        self.can_attack = True

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

class BLA44(AssaultRifle):
    def __init__(self, **kwargs):
        super().__init__(
            model='bla-44',
            scale=.15,
            color=color.gray,
            rotation_y=180,
            name='BLA-44',
            mag_size=30,
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
            mag_size=50,
            mag=50,
            rld_time=3.7,
            delay=.03,
            dmg=10,
            **kwargs
        )

class K412(SniperRifle):
    def __init__(self, **kwargs):
        super().__init__(
            model='K412',
            name='K412',
            mag_size=5,
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
            mag_size=10,
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
            mag_size=8,
            mag=8,
            rld_time=2,
            delay=.5,
            dmg=40,
            **kwargs
        )