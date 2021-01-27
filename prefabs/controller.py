from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController as FPC
from keybinds import keybinds

class Controller(FPC):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def update(self):
        self.speed = 5 + held_keys[keybinds['player_sprint']] * 4

        self.rotation_y += mouse.velocity[0] * self.mouse_sensitivity[1]

        self.camera_pivot.rotation_x -= mouse.velocity[1] * self.mouse_sensitivity[0]
        self.camera_pivot.rotation_x = clamp(self.camera_pivot.rotation_x, -90, 90)

        self.direction = Vec3(
            self.forward * (held_keys[keybinds['player_forward']] - held_keys[keybinds['player_backward']])
            + self.right * (held_keys[keybinds['player_right']] - held_keys[keybinds['player_left']])
        ).normalized()

        origin = self.world_position + (self.up * .5)
        hit_info = raycast(origin, self.direction, ignore=(self,), distance=.5, debug=False)
        if not hit_info.hit:
            self.position += self.direction * self.speed * time.dt

        if self.gravity:
            # gravity
            ray = raycast(self.world_position + (0, 2, 0), self.down, ignore=(self,))
            # ray = boxcast(self.world_position+(0,2,0), self.down, ignore=(self,))

            if ray.distance <= 2.1:
                if not self.grounded:
                    self.land()
                self.grounded = True
                # make sure it's not a wall and that the point is not too far up
                if ray.world_normal.y > .7 and ray.world_point.y - self.world_y < .5:  # walk up slope
                    self.y = ray.world_point[1]
                return
            else:
                self.grounded = False

            # if not on ground and not on way up in jump, fall
            self.y -= min(self.air_time, ray.distance - .05)
            self.air_time += time.dt * .25 * self.gravity
            self.speed = 2

    def input(self, key):
        if key == keybinds['player_jump']:
            self.jump()