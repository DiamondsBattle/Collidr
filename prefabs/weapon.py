from ursina import *
from keybinds import keybinds


class Weapon(Entity):
    def __init__(self,
                 name, dmg,
                 delay,
                 max_range,
                 **kwargs
                 ):

        self.name = name
        self.dmg = dmg
        self.max_range = max_range
        self.delay = delay
        self.can_attack = True

        super().__init__(
            parent=camera,
            always_on_top=True,
            **kwargs
        )

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

class Bullet(Entity):
    def __init__(self,
                 max_range,
                 speed,
                 **kwargs
                 ):

        self.max_range = max_range
        self.speed = speed

        super().__init__(
            model='cube',
            scale=.3,
            world_parent=scene,
            color=color.gray,
            collider='box',
            **kwargs
        )

        b = -(self.position + (self.forward * self.max_range * 10))
        print(b)

        self.animate_position(
            b,
            duration=(self.max_range / self.speed),
            curve=curve.linear,
        )
        self.parent = scene
        invoke(Func(destroy, self), delay=(self.max_range / self.speed))

    # def getCorrectDistance(self):
    #     try:
    #         a = 1 / self.forward[0]
    #         b = 1 / self.forward[1]
    #         c = 1 / self.forward[2]
    #     except Exception:
    #         return 1
    #     print(((a+b+c)/3).__round__())
    #     return ((a+b+c)/3).__round__()

    def update(self):
        # print(self.position)
        i = self.intersects().entity
        if i: # is not None
            print(f'hit: {i}') # FIX : never working

class Gun(Weapon):
    def __init__(self,
                 mag, mag_size,
                 auto, semi,
                 mode, rld_time,
                 ammo, blt_speed,
                 **kwargs
                 ):

        self.mag = mag
        self.mag_size = mag_size
        if self.mag > self.mag_size:
            self.mag = self.mag_size

        self.ammo = ammo

        self.auto = auto
        self.semi = semi
        self.mode = mode
        self.rld_time = rld_time
        self.sht_speed = blt_speed

        self.rlding = False

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

        if key == keybinds['weapon_rld'] and\
                self.can_attack and\
                not self.rlding:
            self.can_attack = False
            self.rlding = True
            invoke(self.reload, delay=self.rld_time)

    def update(self):
        if self.auto and\
                self.mode == 'auto' and\
                held_keys[keybinds['weapon_use_auto']] and\
                self.can_attack and\
                self.mag >= 1:
            self.shoot()

        self.ammo_counter.text = f'{self.mag}/{self.ammo}'

    def shoot(self):
        self.can_attack = False

        self.mag -= 1

        bullet = Bullet(
            max_range=self.max_range,
            speed=self.sht_speed,
            position=self.world_position,
            parent=self,
        )

        if self.mag <= 0 and self.ammo > 0 and\
                not self.can_attack and\
                not self.rlding:
            self.can_attack = False
            self.rlding = True
            invoke(self.reload, delay=self.rld_time)
        else:
            invoke(setattr, self, 'can_attack', True, delay=self.delay)

    def reload(self):
        if self.ammo > 0 and self.mag < 30:
            if self.ammo < self.mag_size:
                dif = self.mag_size - self.mag
                if self.ammo > dif:
                    self.mag += dif
                    self.ammo -= dif
                else:
                    self.mag += self.ammo
                    self.ammo = 0
            else:
                dif = self.mag_size - self.mag
                self.mag = self.mag_size
                self.ammo -= dif

        self.can_attack = True
        self.rlding = False

class SniperRifle(Gun):
    def __init__(self, **kwargs):
        super().__init__(
            auto=False,
            semi=True,
            mode='semi',
            dmg=90,
            max_range=400,
            blt_speed=200,
            **kwargs
        )

class AssaultRifle(Gun):
    def __init__(self, **kwargs):
        super().__init__(
            auto=True,
            semi=False,
            mode='auto',
            max_range=200,
            blt_speed=80,
            **kwargs
        )

class HandGun(Gun):
    def __init__(self, **kwargs):
        super().__init__(
            auto=False,
            semi=True,
            mode='semi',
            max_range=60,
            **kwargs
        )

class SprayGun(Gun):
    def __init__(self, **kwargs):
        super().__init__(
            auto=True,
            semi=False,
            mode='semi',
            max_range=90,
            **kwargs
        )

class BLA44(AssaultRifle):
    def __init__(self, **kwargs):
        super().__init__(
            model='temp',
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