from ursina import *
from direct.stdpy import thread
from settings import video_settings, app_settings, dev_settings
from prefabs.loading_screen import LoadingScreen
from prefabs.main_menu import MainMenu
from prefabs.controller import Controller
from prefabs.weapon import Gun, BLA44, DEagle


def applyVideoSettings():
    window.show_ursina_splash = dev_settings['ursina_splash']
    window.fullscreen = video_settings['window_fullscreen']
    window.windowed_size = video_settings['window_size']
    window.vsync = video_settings['window_vsync']
    window.borderless = False
    window.exit_button.input = None

def applyAppSettings():
    window.title = app_settings['title']

def loadEntities():
    global ld_scr
    for i in range(10000): # dummy load
        print(f'{i}/10000')
    sky = Sky()
    cube = Entity(
        model='cube',
        position=Vec3(0, 0, 10),
        collider='box',
        color=color.red,
    )
    ground = Entity(
        model='map2',
        scale=.01, # Vec3(10, 1, 100),
        collider='mesh',
        color=color.green,
    )
    # ground2 = duplicate(ground)
    # ground2.y = -10
    # ground2.scale = .1
    player = Controller()
    gun = BLA44(
        ammo=666,
        position=Vec3((player.x + 2), (player.y - .5), (player.z + 3.5)),
    )

    ld_scr.cleanDel()

def start():
    applyAppSettings()
    applyVideoSettings()

def playSingleplayer():
    global ld_scr, mm
    ld_scr = LoadingScreen()
    mm.cleanDel()

    thread.start_new_thread(function=loadEntities, args='')

def update():
    pass


if __name__ == '__main__':
    app = Ursina()

    ld_scr = None

    mm = MainMenu(sing=playSingleplayer, multi=None)

    start()

    app.run()