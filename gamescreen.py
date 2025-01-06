from turtle import Screen

class MyScreen(Screen):
    def __init__(self):
        super().__init__()
        self.setup(width=1400, height=1000)
        self.bgcolor("black")


