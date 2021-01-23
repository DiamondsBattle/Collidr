from ursina import *

class HealthBar:
    def __init__(self):
        self.life = 100
        self.bar = Entity(
            model='quad',
            color=color.cyan,
        )

        self.states = {
            100: color.cyan,
            80: color.lime,
            50: color.yellow,
            25: color.orange,
            5: color.red,
        }

        self.changeLife(minus=10)

    def changeLife(self, minus):
        self.life -= minus
        c = self.getColor()
        self.bar.animate('color', c, duration=1)

    def getColor(self):
        for i in self.states:
            print(i)
            if i <= self.life:
                return self.states[i]


if __name__ == '__main__':
    app = Ursina()

    a = HealthBar()

    app.run()