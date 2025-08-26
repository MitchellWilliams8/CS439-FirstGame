import simpleGE, pygame, random

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("Black.png")
        self.lblScore = LblScore()
        self.score = 0
        self.frog = Frog(self)
        self.ground = groundBarrier(self)
        self.fly = Fly(self)
        self.sprites = [self.frog, self.ground, self.fly, self.lblScore]

    def process(self):
        if self.frog.collidesWith(self.fly):
            self.fly.reset()
            self.score -= 1
            self.lblScore.text = f"Score: {self.score}"

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
                self.addForce(20, 90)
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

class Fly(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Fly.png")
        self.setSize(30, 30)
        self.reset()
        #self.position = (500, 400)
    def reset(self):
        self.x = 700
        self.y = 400
        self.dx = random.randint(-8,-4)
        self.dy = random.randint(0, 0)

class LblScore(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.clearBack = True
        self.text = "Score: 0"
        self.center = (100,100)

def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()