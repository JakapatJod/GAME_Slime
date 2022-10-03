import pgzrun
from random import randint

WIDTH = 800
HEIGHT = 600

score = 0
game_over = False

fox = Actor('fox')
fox.pos = 100, 100
coin = Actor('coin')
coin.pos = 200, 200

def draw():
    screen.fill('black')
    fox.draw()
    coin.draw()
    screen.draw.text('Score : '+str(score), color='white',topleft=(10, 10))
    if game_over:
        screen.fill('pink')
        message = 'Final Score :' +str(score)
        screen.draw.text(message, topleft=(10, 10), fontsize=50)

def place_coins():
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HEIGHT - 20))

def update():
    global score
    if keyboard.left:
        fox.x = fox.x - 5
    elif keyboard.right:
        fox.x = fox.x + 5
    elif keyboard.up:
        fox.y = fox.y - 5
    elif keyboard.down: 
        fox.y = fox.y + 5

    if fox.x >(800):
        fox.x = (1)

    elif fox.x < (1):
        fox.x = (800)

    elif fox.y > (600):
        fox.y = (1)

    elif fox.y < (1):
        fox.y = (600)

    coin_collected = fox.colliderect(coin)
    if coin_collected:
        place_coins()
        score += 1

def time_up():
    global game_over
    game_over = True

clock.schedule(time_up, 10.0)
place_coins()
pgzrun.go()