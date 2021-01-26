from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController as FPC

class Controller(FPC):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.direction = Vec3(
            self.forward * (held_keys['z'] - held_keys['s'])
            + self.right * (held_keys['d'] - held_keys['q'])
        ).normalized()