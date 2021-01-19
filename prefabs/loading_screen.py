from ursina import *

class LoadingScreen:
    def __init__(self):
        self.bg = Entity(
            model='quad',
            color=color.black,
        )
        self.bg.scale *= 400
        self.text = Text(
            text='Loading...',
        )

    def cleanDel(self):
        destroy(self.bg)
        destroy(self.text)
        del self


if __name__ == '__main__':
    app = Ursina()

    a = LoadingScreen()

    app.run()