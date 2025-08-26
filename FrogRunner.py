import simpleGE, pygame

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("Black.png")
        self.frog = Frog(self)
        self.barrier = Barrier(self)
        self.sprites = [self.frog, self.barrier]


class Frog(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Frog.png")
        self.setSize(50, 50)
        self.position = (50, 400)

    def process(self):
        self.addForce(1, 270)
        if self.collidesWith(self.scene.barrier):
            self.dx=0
            self.dy=0
        if self.scene.isKeyPressed(pygame.K_SPACE):
            self.dy = 0
            self.addForce(5, 90)




class Barrier(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Barrier.png")
        self.setSize(1400, 50)
        self.position = (50, 450)

def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()