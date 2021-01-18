from ursina import *

class LoadingScreen(Entity):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.bg = Entity(
            model='quad',
            color=color.black,
        )
        self.bg.scale *= 400
        self.text = Text('Loading...')


if __name__ == '__main__':
    app = Ursina()

    a = LoadingScreen()

    app.run()