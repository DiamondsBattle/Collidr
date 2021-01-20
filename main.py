from ursina import *
from direct.stdpy import thread
from settings import video_settings, dev_settings
from prefabs.loading_screen import LoadingScreen


def applyVideoSettings():
    window.show_ursina_splash = dev_settings['ursina_splash']
    window.fullscreen = video_settings['window_fullscreen']
    window.windowed_size = video_settings['window_size']
    window.vsync = video_settings['window_vsync']
    window.borderless = False

def loadEntities():
    global ld_scr
    sky = Sky()
    ground = Entity(
        model='cube',
        scale=Vec3(10, 1, 10),
        collider='cube',
        color=color.green,
    )
    ld_scr.cleanDel()

def start():
    applyVideoSettings()
    thread.start_new_thread(function=loadEntities, args='')

def update():
    pass


if __name__ == '__main__':
    app = Ursina()

    ld_scr = LoadingScreen()

    start()

    app.run()