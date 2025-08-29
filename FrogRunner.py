import pygame
import random
import simpleGE
import time

"""

Background and Ground:
ansimuz: https://opengameart.org/content/sunnyland-forest-of-illusion

Sound Effects:
Buzz - nosycat: https://opengameart.org/content/buzz-grid-sounds
Death - nosycat: https://opengameart.org/content/buzz-grid-sounds
Explode - nosycat: https://opengameart.org/content/buzz-grid-sounds
Points - nosycat: https://opengameart.org/content/buzz-grid-sounds
Snap - AntumDeluge: https://opengameart.org/content/thwack-sounds
Screech - AntumDeluge: https://opengameart.org/content/barn-owl-screech

"""

# Game scene
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()

        self.setImage("Back.png")

        #pygame.mixer.music.load("")
        #pygame.mixer.music.play()

        self.explode = simpleGE.Sound("Explode.wav")
        self.points = simpleGE.Sound("Points.wav")
        self.buzz = simpleGE.Sound("Buzz.wav")
        self.snap = simpleGE.Sound("Snap.wav")
        self.screech = simpleGE.Sound("Screech.flac")
        self.death = simpleGE.Sound("Death.wav")

        self.lblScore = LblScore()
        self.lblHealth = LblHealth()
        self.score = 0
        self.health = 100

        self.frog = Frog(self)
        self.foreground1 = Foreground1(self)
        self.foreground2 = Foreground2(self)
        self.ground = groundBarrier(self)
        self.fly = Fly(self)
        self.platform1 = Platform1(self)
        self.platform2 = Platform2(self)
        self.goldScarab = goldScarab(self)
        self.beetle = Beetle(self)
        self.projectile = Projectile(self)
        self.jewel = Jewel(self)
        self.bird = Bird(self)
        self.explosion = Explosion(self)
        self.sprites = [self.foreground1, self.foreground2, self.frog, self.ground, self.fly,
                        self.lblScore, self.platform1, self.platform2, self.goldScarab,
                        self.beetle, self.projectile, self.lblHealth, self.jewel,
                        self.bird, self.explosion]

    def process(self):
        if self.frog.collidesWith(self.fly):
            self.fly.reset()
            self.score -= 5
            self.buzz.play()
            self.lblScore.text = f"Score: {self.score}"

        if self.frog.collidesWith(self.goldScarab):
            self.goldScarab.reset()
            self.score += 3
            self.points.play()
            self.lblScore.text = f"Score: {self.score}"

        if self.frog.collidesWith(self.jewel):
            self.jewel.reset()
            self.score += 10
            self.points.play()
            self.lblScore.text = f"Score: {self.score}"

        if self.frog.collidesWith(self.beetle):
            self.beetle.reset()
            self.health -= 25
            self.snap.play()
            self.lblHealth.text = f"Health: {self.health}"

        if self.frog.collidesWith(self.bird):
            self.health -= 90
            self.screech.play()
            self.lblHealth.text = f"Health: {self.health}"

        if self.projectile.collidesWith(self.fly):
            self.explosion.explode()
            self.explode.play()
            self.fly.reset()
            self.projectile.reset()

        if self.projectile.collidesWith(self.beetle):
            self.explosion.explode()
            self.explode.play()
            self.projectile.reset()

        if self.projectile.collidesWith(self.bird):
            self.explosion.explode()
            self.explode.play()
            self.projectile.reset()

        # Game over factor
        if self.health <= 0:
            self.death.play()
            time.sleep(1.5)
            self.stop()

        # Resets sprites when they reach the left side of screen
        # This Randomizes their speed instead of just wrapping
        if self.platform1.x < 10:
            self.platform1.reset()
        if self.platform2.x < 10:
            self.platform2.reset()
        if self.fly.x < 10:
            self.fly.reset()
        if self.beetle.x < 10:
            self.beetle.reset()
        if self.goldScarab.x < 10:
            self.goldScarab.reset()
        if self.jewel.x < 10:
            self.jewel.reset()
        if self.bird.x < 10:
            self.bird.reset()

# Player sprite
class Frog(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Frog.png")
        self.setSize(60, 50)
        self.position = (50, 400)
        self.inAir = True
        self.setBoundAction(self.CONTINUE)

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

        if self.collidesWith(self.scene.platform1):
            if self.dy > 0:
                self.bottom = self.scene.platform1.top
                self.dy = 0
                self.inAir = False

        if self.collidesWith(self.scene.platform2):
            if self.dy > 0:
                self.bottom = self.scene.platform2.top
                self.dy = 0
                self.inAir = False

# Foreground 1
class Foreground1 (simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Foreground.png")
        self.setSize(700, 500)
        self.setBoundAction(self.CONTINUE)
        self.dx = -1
        self.reset()
    def process(self):

        if self.right <= -0:
            self.left = self.scene.foreground2.right

    def reset(self):
        self.position = (350, 200)

# Foreground 2
class Foreground2 (simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Foreground.png")
        self.setSize(700, 500)
        self.setBoundAction(self.CONTINUE)
        self.dx = -1
        self.reset()

    def process(self):
        if self.right <= 0:
            self.left = self.scene.foreground1.right


    def reset(self):
        self.position = (1050, 200)

# Ground
class groundBarrier(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Ground.png")
        self.setSize(700, 60)
        self.position = (300, 455)

# Moving platform 1
class Platform1 (simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.colorRect("blue",(100,20))
        self.reset()

    def reset(self):
        self.x = 640
        self.y = 300
        self.dx = random.randint(-10, -2)
        self.dy = random.randint(0, 0)

# Moving platform 2
class Platform2(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.colorRect("purple",(75,20))
        self.reset()

    def reset(self):
        self.x = 640
        self.y = 150
        self.dx = random.randint(-4, -1)
        self.dy = random.randint(0, 0)

# Enemy 1
class Fly(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Fly.png")
        self.setSize(45, 45)
        self.reset()


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
        self.setSize(100, 55)
        self.reset()

    def reset(self):
        self.x = 625
        self.y = 400
        self.dx = random.randint(-8,-4)
        self.dy = random.randint(0, 0)

# Enemy 3
class Bird(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Bird.png")
        self.setSize(80, 75)
        self.reset()

    def reset(self):
        self.x = 625
        self.y = 50
        self.dx = random.randint(-2,-1)
        self.dy = random.randint(0, 0)

# Scoring object 1
class goldScarab(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("goldScarab.png")
        self.setSize(40, 40)
        self.reset()

    def reset(self):
        self.x = 625
        self.y = 200
        self.dx = random.randint(-8,-4)
        self.dy = random.randint(0, 0)

# Scoring object 2
class Jewel(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Jewel.png")
        self.setSize(40, 30)
        self.reset()

    def reset(self):
        self.x = 625
        self.y = 100
        self.dx = random.randint(-4,-1)
        self.dy = random.randint(0, 0)

# Projectile
class Projectile(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Projectile.png")
        self.setSize(70, 25)
        self.setBoundAction(self.HIDE)
        self.hide()

    def shoot(self):
        if not self.visible:
            self.show()
            self.position = (self.scene.frog.x, self.scene.frog.y)
            self.speed = 7

    def reset(self):
        self.hide()

# Explosion effect
class Explosion(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.oldPosition = None
        self.setImage("Explosion.png")
        self.setSize(100, 100)
        self.reset()
        self.timer = simpleGE.Timer()
        self.timer.totalTime = .5

    def explode(self):
        pos = self.position = (self.scene.projectile.x, self.scene.projectile.y)
        self.oldPosition = pos
        self.show()
        self.timer.start()

    def process(self):
        if self.visible and self.timer.getElapsedTime() >= .5:
            self.reset()

    def reset(self):
        self.hide()

# Score
class LblScore(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.clearBack = True
        self.text = "Score: 0"
        self.center = (60,25)

# Health
class LblHealth(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.clearBack = True
        self.text = "Health: 100"
        self.center = (200,25)

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
        self.lblInstructions.center = (320, 140)
        self.lblInstructions.size = (400, 200)

        self.lblScore = simpleGE.Label()
        self.lblScore.center = (320, 320)
        self.lblScore.size = (250, 60)
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

# main
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