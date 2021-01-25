from ursina import *

class MainMenu:
    def __init__(self, sing, multi):
        self.bg = Entity(
            model='quad',
            texture='main_menu',
            scale=Vec3(15, 8.5, 0),
        )
        self.sing = Button(
            icon='btn_sing',
            position=Vec3(-.55, .1, 0),
            scale=Vec3(.6, .2, 0),
            on_click=sing,
        )
        self.multi = Button(
            icon='btn_multi',
            position=Vec3(-.55, -.2, 0),
            scale=Vec3(.6, .2, 0),
            on_click=multi,
        )
        self.settings = Button(
            texture='btn_sett',
            position=Vec3(),
            enabled=False,
        )
        self.quit = Button(
            texture='btn_quit',
            position=Vec3(),
            enabled=False,
        )

    def cleanDel(self):
        destroy(self.bg)
        destroy(self.sing)
        destroy(self.multi)
        destroy(self.settings)
        destroy(self.quit)
        del self