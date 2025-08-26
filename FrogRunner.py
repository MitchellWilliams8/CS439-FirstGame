import simpleGE, pygame, random

# Game scene
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("Black.png")
        self.setSize = (1000,1000)
        self.lblScore = LblScore()
        self.score = 0
        self.frog = Frog(self)
        self.ground = groundBarrier(self)
        self.fly = Fly(self)
        self.platform = Platform(self)
        self.goldScarab = goldScarab(self)
        self.beetle = Beetle(self)
        self.projectile = Projectile(self)
        self.sprites = [self.frog, self.ground, self.fly,
                        self.lblScore, self.platform, self.goldScarab,
                        self.beetle, self.projectile]

    def process(self):
        if self.frog.collidesWith(self.fly):
            self.fly.reset()
            self.score -= 1
            self.lblScore.text = f"Score: {self.score}"

        if self.frog.collidesWith(self.goldScarab):
            self.goldScarab.reset()
            self.score += 3
            self.lblScore.text = f"Score: {self.score}"

        if self.frog.collidesWith(self.beetle):
            self.beetle.reset()
            self.score -= 2
            self.lblScore.text = f"Score: {self.score}"

        if self.projectile.collidesWith(self.fly):
            self.fly.reset()
            self.projectile.reset()

        if self.projectile.collidesWith(self.beetle):
            self.projectile.reset()

# Player sprite
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
        if self.scene.isKeyPressed(pygame.K_s):
            self.scene.projectile.shoot()

        self.inAir = True
        if self.collidesWith(self.scene.ground):
            if self.dy > 0:
                self.bottom = self.scene.ground.top
                self.dy = 0
                self.inAir = False

        if self.collidesWith(self.scene.platform):
            if self.dy > 0:
                self.bottom = self.scene.platform.top
                self.dy = 0
                self.inAir = False

# Ground
class groundBarrier(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Ground.png")
        self.setSize(1400, 50)
        self.position = (50, 450)

# Moving platform
class Platform(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.colorRect("blue",(100,20))
        self.reset()
    def reset(self):
        self.x = 700
        self.y = 300
        self.dx = random.randint(-8, -4)
        self.dy = random.randint(0, 0)

# Enemy 1
class Fly(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Fly.png")
        self.setSize(30, 30)
        self.reset()
        #self.position = (500, 400)
    def reset(self):
        self.x = 625
        self.y = 275
        self.dx = random.randint(-8,-4)
        self.dy = random.randint(0, 0)


# Enemy 2
class Beetle(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Beetle.png")
        self.setSize(75, 75)
        self.reset()

    def reset(self):
        self.x = 625
        self.y = 400
        self.dx = random.randint(-8,-4)
        self.dy = random.randint(0, 0)

# Scoring object
class goldScarab(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("goldScarab.png")
        self.setSize(30, 30)
        self.reset()
    def reset(self):
        self.x = 625
        self.y = 200
        self.dx = random.randint(-8,-4)
        self.dy = random.randint(0, 0)

# Projectile
class Projectile(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Projectile.png")
        self.setSize(50, 50)
        self.setBoundAction(self.reset())

    def shoot(self):
        self.position = (self.scene.frog.x, self.scene.frog.y)
        self.speed = 7

    def reset(self):
        self.position = (-100, -100)
        self.speed = 0

# Score
class LblScore(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.clearBack = True
        self.text = "Score: 0"
        self.center = (60,25)

# Intro
class Intro(simpleGE.Scene):
    def __init__(self, score = 0):
        super().__init__()
        self. status = "quit"
        self.score = score
        self.setImage("black.png")
        #pygame.mixer.music.load("intro.mp3")
        #pygame.mixer.music.play()
        self.lblInstructions = simpleGE.MultiLabel()
        self.lblInstructions.textLines = [
            "Instructions"
        ]
        self.lblInstructions.center = (320, 240)
        self.lblInstructions.size = (600, 600)
        self.lblScore = simpleGE.Label()
        self.lblScore.center = (320, 240)
        self.lblScore.size = (600, 600)
        self.lblScore.text = f"Previous Score: {self.score}"
        self.btnPlay = simpleGE.Button()
        self.btnPlay.center = (150,400)
        self.btnPlay.text = "Play"
        self.btnQuit = simpleGE.Button()
        self.btnQuit.center = (500, 400)
        self.btnQuit.text = "Quit"
        self.sprites = [self.lblInstructions, self.lblScore, self.btnPlay, self.btnQuit]

    def process(self):
        if self.btnPlay.clicked:
            self.status = "play"
            self.stop()
        if self.btnQuit.clicked:
            self.status = "quit"
            self.stop()


def main():
    keepGoing = True
    score = 0

    while keepGoing:
        intro = Intro(score)
        intro.start()

        if intro.status == "quit":
            keepGoing = False
        else:
            game = Game()
            game.start()
            score = game.score

if __name__ == "__main__":
    main()