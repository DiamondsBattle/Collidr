from ursina import *
from direct.stdpy import thread
from settings import video_settings, dev_settings

def applyVideoSettings():
    if dev_settings['ursina_splash']:
        window.show_ursina_splash = True

    window.fullscreen = video_settings['window_fullscreen']
    if not window.fullscreen:
        window.size = video_settings['window_size']

    window.vsync = video_settings['window.vsync']

def loadEntities():
    pass

def start():
    applyVideoSettings()

def update():
    pass


if __name__ == '__main__':
    app = Ursina()

    start()

    app.run()