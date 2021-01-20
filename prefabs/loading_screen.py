from ursina import *
from tips import tips
from random import randint

class LoadingScreen:
    def __init__(self):
        self.bg = Entity(
            model='quad',
            texture='loading_screen',
            scale=Vec3(15, 8.5, 0),
        )
        self.text = Text(
            text='Loading.',
            scale=2,
            position=Vec3(.55, -.4, 0),
        )
        self.tip = Text(
            text='',
            scale=1.3,
            position=Vec3(-.75, -.11, 0)
        )

        invoke(self.changeText, delay=1)
        self.showRandomTip()

    def cleanDel(self):
        destroy(self.bg)
        destroy(self.text)
        del self

    def changeText(self):
        if self.text.text == 'Loading.':
            self.text.text = 'Loading..'
        elif self.text.text == 'Loading..':
            self.text.text = 'Loading...'
        else:
            self.text.text = 'Loading.'
        invoke(self.changeText, delay=1)

    def showRandomTip(self):
        r = randint(0, len(tips) - 1) # Avoid the example placeholder
        print(r)
        self.tip.text = tips[r]


if __name__ == '__main__':
    app = Ursina()

    a = LoadingScreen()

    app.run()