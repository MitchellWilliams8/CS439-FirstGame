import simpleGE, pygame

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("Black.png")
        self.frog = Frog(self)
        self.ground = groundBarrier(self)
        self.sprites = [self.frog, self.ground]

class Frog(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Frog.png")
        self.setSize(50, 50)
        self.position = (50, 400)
        self.inAir = True

    def process(self):
        if self.inAir:
            self.addForce(1, 270)

        if self.y > 500:
            self.inAir =False
            self.y = 500
            self.dy = 0

        if self.scene.isKeyPressed(pygame.K_SPACE):
            if not self.inAir:
                self.addForce(15, 90)
                self.inAir = True

        self.inAir = True
        if self.collidesWith(self.scene.ground):
            if self.dy > 0:
                self.bottom = self.scene.ground.top
                self.dy = 0
                self.inAir = False

class groundBarrier(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Ground.png")
        self.setSize(1400, 50)
        self.position = (50, 450)

def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()