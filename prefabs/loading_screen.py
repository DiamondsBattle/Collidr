from ursina import *

class LoadingScreen:
    def __init__(self):
        self.bg = Entity(
            model='quad',
            color=color.black,
            parent=self,
        )
        self.bg.scale *= 400
        self.text = Text(
            text='Loading...',
            parent=self,
        )


if __name__ == '__main__':
    app = Ursina()

    a = LoadingScreen()

    app.run()