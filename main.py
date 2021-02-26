from ursina import *
from direct.stdpy import thread
from settings import video_settings, app_settings, dev_settings
from prefabs.loading_screen import LoadingScreen
from prefabs.main_menu import MainMenu
from prefabs.controller import Controller
from prefabs.weapon import Gun, BLA44, DEagle


class Game(Ursina):
    def __init__(self, spawn):
        super().__init__()

        self.spawn = spawn

        self.ld_scr = None

        self.mm = MainMenu(
            multi=None,
            sing=self.playSingleplayer,
        )

    @staticmethod
    def applyVideoSettings():
        window.show_ursina_splash = dev_settings['ursina_splash']
        window.fullscreen = video_settings['window_fullscreen']
        window.windowed_size = video_settings['window_size']
        window.vsync = video_settings['window_vsync']
        window.borderless = False
        window.exit_button.input = None

    @staticmethod
    def applyAppSettings():
        window.title = app_settings['title']

    def loadEntities(self):
        for i in range(10000): # dummy load
            print(f'{i}/10000')
        self.sky = Sky()
        self.cube = Entity(
            model='cube',
            position=Vec3(0, 0, 10),
            collider='box',
            color=color.red,
        )
        self.ground = Entity(
            model='map2',
            scale=.01, # Vec3(10, 1, 100),
            collider='mesh',
            color=color.green,
        )
        self.player = Controller(
            position=self.spawn
        )
        self.gun = BLA44(
            ammo=666,
            position=Vec3((self.player.x + 2), (self.player.y - .5), (self.player.z + 3.5)),
        )

        self.ld_scr.cleanDel()

    def start(self):
        self.applyAppSettings()
        self.applyVideoSettings()

    def playSingleplayer(self):
        self.ld_scr = LoadingScreen()
        self.mm.cleanDel()

        thread.start_new_thread(function=self.loadEntities, args='')

    def update(self):
        pass


if __name__ == '__main__':
    game = Game(spawn=Vec3(0,0,0))

    game.start()

    game.run()