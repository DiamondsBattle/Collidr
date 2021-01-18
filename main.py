from ursina import *
from direct.stdpy import thread
from settings import video_settings, dev_settings


def applyVideoSettings():
    if dev_settings['ursina_splash']:
        window.show_ursina_splash = True

    window.fullscreen = video_settings['window_fullscreen']
    if not window.fullscreen:
        window.size = video_settings['window_size']

    window.vsync = video_settings['window_vsync']

def loadEntities():
    sky = Sky()
    ground = Entity(
        model='cube',
        scale=Vec3(10, 1, 10),
        collider='cube',
        color=color.green,
    )


def showLoadingScreen():
    pass

def start():
    applyVideoSettings()
    showLoadingScreen()
    try:
        t = thread.start_new_thread(function=loadEntities)
    except Exception:
        print('unable to start a thread')


def update():
    pass


if __name__ == '__main__':
    app = Ursina()

    loading = LoadingScreen()

    start()

    app.run()
