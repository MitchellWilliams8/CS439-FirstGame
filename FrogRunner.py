import simpleGE, pygame

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("Black.png")
        self.frog = Frog(self)
        self.sprites = [self.frog]


class Frog(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Frog.png")
        self.setSize(50, 50)
        self.position = (50, 450)



def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()