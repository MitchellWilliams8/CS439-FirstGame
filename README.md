# CS439-FirstGame

Game Design Document

# Overview:
This game is sort of an endless runner/platformer game. Enemies and platforms will scroll by on the screen. The main character is able to shoot a projectile and jump. There are platforms that can be jumped on to avoid enemies or reach items. The goal is to avoid the enemies and collect items to get the highest possible score. One type of enemy can be stopped with the projectile while the others are resistent. The enemies can take away health/points. Once health reaches zero the game ends.

# Assets:

Sprites:

One player asset that can be controlled
  
  - The player is a frog with a rocket launcher that can jump and shoot
    
Three enemy assets. These assets all move across the screen towards the left at different intervals of speed and are reset once they reach the far left.
  
  - Fly. The fly takes away 5 points from the player upon contact and can be taken out by projectiles
  - Beetle. The beetle takes away 25 health from the player upon contact and is resistent to projectiles
  - Bird. The bird takes away 90 health from the player upon contact and is resistent to projectiles.
  
Two scoring assets. These assets all move across the screen towards the left at different intervals of speed and are reset once they reach the far left.
  
  - Gold Scarab. The golden scarab adds 3 points to the players score upon contact.
  - Jewel. The jewel adds 10 points to the players score upon contact.
    
One projectile asset
  
  - The projectile can be fired by the player only when it is not visible on screen. The projectile asset resets the fly asset upon contact.
    
One explosion effect asset
  
  - The explosion asset replaces the projectile upon contact with another asset and is reset after 0.5 seconds.
    
Two platform assets. These assets all move across the screen towards the left at different intervals of speed and are reset once they reach the far left.
  
  - There is a blue platform and a purple shorter platform at different heights that can be jumped on by the frog and jumped off of.
    
Two foreground assets. These assets all move across the screen towards the left at a set speed and are reset once they reach the far left.
  
  - These assets scroll by in the background to give the visual effect of movement.
    
One ground asset
  
  - The ground acts as the bottom of the game that the frog can jump off of.

Labels:

- One score label. Starts at 0.
- One health label. Starts at 100.

Buttons:

-Start button and Quit button on title screen.

# Credits for borrowed assets:
Music:
Matthew Pablo - https://opengameart.org/content/space-dimensions-8bitretro-version
DST -https://opengameart.org/content/tower-defense-theme

Background and Ground:
ansimuz - https://opengameart.org/content/sunnyland-forest-of-illusion

Sound Effects:
Buzz - nosycat: https://opengameart.org/content/buzz-grid-sounds
Death - nosycat: https://opengameart.org/content/buzz-grid-sounds
Explode - nosycat: https://opengameart.org/content/buzz-grid-sounds
Points - nosycat: https://opengameart.org/content/buzz-grid-sounds
Snap - AntumDeluge: https://opengameart.org/content/thwack-sounds
Screech - AntumDeluge: https://opengameart.org/content/barn-owl-screech

# Milestones:
- Get the scene with a sprite on it.
- Add gravity to the sprite and give it a ground platform.
- Add an enemy sprite that moves across the screen.
- Add conatct between the enemy and player.
- Add additional platforms that can be jumped on.
- Add an item that can be collected to increase score.
- Add a projectile that can collide with an enemy.
- Add additional enemies and scoring item.
- Add intro scene and sound effects.
- Finishing touches such as background music replacing the placeholders.
