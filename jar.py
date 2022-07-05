import random
import sys
import os

WIDTH = 1080
HEIGHT = 720
TITLE = "JAR Jump And Run"

cwd = os.getcwd()
fsave = open(cwd + "\highscore.txt", "r")
fsavev = str(fsave.read())

Clouds = []

# 66x92
player = Actor("alien_r")
player.x = 50
player.y = 500
pvx = 0
pvy = 0
isonground =  0
keyadown = 0
keyddown = 0
highscore = int(fsavev)
score = 0


class Block():

    def __init__(self, p1x, p1y, width, height):
        self.p1x = p1x
        self.p1y = p1y
        self.width = width
        self.height = height
        self.rect = Rect((p1x, p1y), (width, height))

    def drawBlock(self):
        screen.draw.filled_rect(self.rect, (255, 255, 255))
        screen.draw.filled_circle((self.p1x + 20, self.p1y + 20), 34, (255, 255, 255))
        screen.draw.filled_circle((self.p1x + self.width - 20, self.p1y + 20), 34, (255, 255, 255))
        screen.draw.filled_circle((self.p1x + self.width / 2, self.p1y + 20), 33, (255, 255, 255))
        screen.draw.filled_circle((self.p1x + 20, self.p1y + self.height - 20), 34, (255, 255, 255))
        screen.draw.filled_circle((self.p1x + self.width - 20, self.p1y + self.height - 20), 34, (255, 255, 255))
        screen.draw.filled_circle((self.p1x + self.width / 2, self.p1y + self.height - 20), 33, (255, 255, 255))
        screen.draw.filled_circle((self.p1x + 20, self.p1y + self.height / 2), 38, (255, 255, 255))
        screen.draw.filled_circle((self.p1x + self.width - 20, self.p1y + self.height / 2), 38, (255, 255, 255))

    def checkfeetcol(self, pposx, pposy):
        pcolpos1 = [pposx - 25, pposy + 46]
        pcolpos2 = [pposx + 25, pposy + 46]
        bcolpos1 = [self.p1x, self.p1y]
        bcolpos2 = [self.p1x + self.width, self.p1y]
        col = 0
        if (
            pcolpos1[0] <= bcolpos2[0]
            and pcolpos1[0] >= bcolpos1[0]
            and pcolpos1[1] >= bcolpos1[1]
        ):
            col = 1
        elif (
            pcolpos2[0] <= bcolpos2[0]
            and pcolpos2[0] >= bcolpos1[0]
            and pcolpos2[1] >= bcolpos1[1]
        ):
            col = 1
        return col

def new_level():
    global score
    global Blocks
    global highscore
    global fsave
    global fsavev
    Blocks = []
    Blocks.append(Block(0, 650, 100, 70))
    b2x = random.randint(200, 300)
    Blocks.append(Block(b2x, 650 , 100, 70))
    b3x = random.randint(b2x + 200, b2x + 290)
    Blocks.append(Block(b3x, 650 , 100, 70))
    b4x = random.randint(b3x + 200, b3x + 290)
    Blocks.append(Block(b4x, 650 , 100, 70))
    b5x = random.randint(b4x + 200, b4x + 290)
    Blocks.append(Block(b5x, 650 , 100, 70))
    score += 1
    if score > highscore:
        highscore = score
        fsave = open(cwd + "\highscore.txt", "w")
        fsave.write(str(highscore))
        fsave = open(cwd + "\highscore.txt", "r")
        fsavev = fsave.read()

def draw():
    global Blocks
    screen.fill((183, 233, 247))
    player.draw()
    for block in Blocks:
        block.drawBlock()
    for cloud in Clouds:
        cloud.draw()
    screen.draw.text("Score:" + str(score), [10, 5], color="black")
    screen.draw.text("Highcore:" + str(highscore), [10, 20], color="black")

def on_key_down(key):
    global pvx
    global pvy
    global keyadown
    global keyddown
    global isonground
    if key == keys.D:
        pvx = 2
        player.image = "alien_r"
        keyddown = 1
    elif key == keys.A:
        player.image = "alien_l"
        pvx = -2
        keyadown = 1
    elif key == keys.SPACE and isonground == 1:
        pvy = -4


def on_key_up(key):
    global keyadown
    global keyddown
    global pvx
    if key == keys.D:
        keyddown = 0
        if keyadown == 0:
            pvx = 0
    elif key == keys.A:
        if keyddown == 0:
            pvx = 0
        keyadown = 0

def moveplayer():
    global isonground
    global pvx
    global pvy
    if isonground == 1 and pvy > 0:
        pvy = 0
    player.x = player.x + pvx
    player.y = player.y + pvy
    if player.x > 1080:
        player.x = 0
        new_level()
    if player.y > 700:
        sys.exit(0)

def gravity():
    global pvy
    global isonground
    isonground = 0
    for block in Blocks:
        if block.checkfeetcol(player.x, player.y) == 1:
            isonground = 1
    if isonground == 0:
        pvy += 0.1

def move_clouds():
    for cloud in Clouds:
        cloud.x += -1
        if cloud.x < -300:
            Clouds.remove(cloud)
            print("removed a cloud")

def game_update():
    gravity()
    moveplayer()
    move_clouds()

def cloud_update():
    print("cloud")
    cloud_len = len(Clouds)
    cloud_texture = random.randint(1, 4)
    if cloud_texture ==  1:
        Clouds.append(Actor("cloud1.png"))
    elif cloud_texture == 2:
        Clouds.append(Actor("cloud2.png"))
    elif cloud_texture == 3:
        Clouds.append(Actor("cloud3.png"))
    elif cloud_texture == 4:
        Clouds.append(Actor("cloud4.png"))

    Clouds[cloud_len].x = 1400
    Clouds[cloud_len].y = random.randint(0, 400)


new_level()
clock.schedule_interval(game_update, 0.01)
clock.schedule_interval(cloud_update, 10)
clock.schedule_interval(cloud_update, 7)
clock.schedule_interval(cloud_update, 5)
