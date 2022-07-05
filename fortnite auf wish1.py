import random
import os

WIDTH = 1080
HEIGHT = 720
TITLE = "fortnite auf wish"

cwd = os.getcwd()
fsave = open(cwd + "\highscore.txt", "r")
fsavev = str(fsave.read())

# 66 x 92
player = Actor("alien_r")
player.x = 50
player.y = 674
pvx = 0
pvy = 0
prange = 170
pspeed = 2

crosshair = Actor("crosshair")

# 66 x 92
banana = Actor("banana_l")
banana.x = 1030
banana.y = 674
bspeed = 1

ammo = Actor("ammo5")
ammo.x = 1020
ammo.y = 20
cap = 5

health = Actor("healthbar5")
health.x = 60
health.y = 20
hvalue = 5

ammop = Actor("ammo")
ammop.x = -1200
ammop.y = 700
apos = 0
ammop_fs_time = 500

healthp = Actor("medkit")
healthp.x = -1200
healthp.y = 700
mkos = 0
healthp_fs_time = 1500

weapon = Actor("ar")
weapon.x = 930
weapon.y = 40
wapon = 2

highscore = int(fsavev)
score = 0


def draw():
    global prange
    screen.fill((208, 61, 51))
    screen.draw.filled_circle([player.x, player.y], prange, (239, 23, 58))
    screen.draw.circle([player.x, player.y], prange, (199, 28, 0))
    screen.draw.circle([player.x, player.y], prange - 1, (199, 28, 0))
    screen.draw.circle([player.x, player.y], prange - 2, (199, 28, 0))
    screen.draw.circle([player.x, player.y], prange - 3, (199, 28, 0))
    player.draw()
    banana.draw()
    ammo.draw()
    health.draw()
    ammop.draw()
    healthp.draw()
    screen.draw.text("Score:" + str(score), [120, 5], color="black")
    screen.draw.text("Highcore:" + str(highscore), [120, 20], color="black")
    crosshair.draw()
    weapon.draw()


def on_mouse_move(pos):
    crosshair.x = pos[0]
    crosshair.y = pos[1]


def on_key_down(key):
    global cap
    global pvx
    global wapon
    global pspeed
    if key == keys.D:
        pvx = pspeed
        player.image = "alien_r"
    elif key == keys.A:
        player.image = "alien_l"
        pvx = -pspeed
    elif key == keys.K_1:
        wapon = 1
    elif key == keys.K_2:
        wapon = 2
    elif key == keys.K_3:
        wapon = 3


def on_key_up(key):
    global pvx
    if key == keys.D:
        pvx = 0
    elif key == keys.A:
        pvx = 0


def moveplayer():
    global pvx
    global pvy
    player.x = player.x + pvx
    player.y = player.y + pvy


def banana_move():
    global bspeed
    if player.x > banana.x:
        banana.x += bspeed
        banana.image = "banana_r"
    if player.x < banana.x:
        banana.x += -bspeed
        banana.image = "banana_l"


def on_mouse_down(pos, button):
    bprange = player.x - banana.x
    if bprange < 0:
        bprange = bprange * -1
    global score
    global cap
    global bspeed
    global prangeS
    global highscore

    if cap > 0:
        sounds.shot.play()
    if (
        button == mouse.LEFT
        and banana.collidepoint(pos)
        and cap > 0
        and bprange <= prange
    ):
        if random.randint(0, 1) == 1:
            banana.x = 50
        else:
            banana.x = 1030
        score += 1
        bspeed += 0.05
        if score > highscore:
            highscore = score
        fsave = open(cwd + "\highscore.txt", "w")
        fsave.write(str(highscore))
        fsave = open(cwd + "\highscore.txt", "r")
        fsavev = fsave.read()
    cap += -1

def player_check():
    global hvalue
    bprange = player.x - banana.x
    if bprange < 0:
        bprange = bprange * -1
    if bprange <= 3:
        sounds.amogus.play()
        if random.randint(0, 1) == 1:
            banana.x = 50
        else:
            banana.x = 1030
        hvalue += -1
    if player.x < 0:
        player.x = 1080
    if player.x > 1080:
        player.x = 0


def ammo_update():
    global cap
    if cap == 0:
        ammo.image = "ammo0"
    elif cap == 1:
        ammo.image = "ammo1"
    elif cap == 2:
        ammo.image = "ammo2"
    elif cap == 3:
        ammo.image = "ammo3"
    elif cap == 4:
        ammo.image = "ammo4"
    elif cap == 5:
        ammo.image = "ammo5"


def ammop_check():
    global ammop_fs_time
    global cap
    global apos
    parange = ammop.x - player.x
    if parange < 0:
        parange = parange * (-1)
    if parange <= 10:
        apos = 0
        ammop.x = -1000
        cap = 5
    if apos == 0:
        ammop_fs_time += 1
    if ammop_fs_time >= 500:
        apos = 1
        ammop_fs_time = 0
        ammop.x = random.randint(20, 1060)


def health_update():
    global hvalue
    if hvalue >= 6:
        hvalue = 5
    if hvalue == 0:
        health.image = "healthbar0"
    elif hvalue == 1:
        health.image = "healthbar1"
    elif hvalue == 2:
        health.image = "healthbar2"
    elif hvalue == 3:
        health.image = "healthbar3"
    elif hvalue == 4:
        health.image = "healthbar4"
    elif hvalue == 5:
        health.image = "healthbar5"
    if hvalue <= 0:
        player.x = -100000000
        banana.x = -100000000


def healthp_update():
    global healthp_fs_time
    global hvalue
    global mkos
    mkrange = healthp.x - player.x
    if mkrange < 0:
        mkrange = mkrange * (-1)
    if mkrange <= 10:
        mkos = 0
        healthp.x = -1000
        hvalue += 2
    if mkos == 0:
        healthp_fs_time += 1
    if healthp_fs_time >= 1500:
        mkos = 1
        healthp_fs_time = 0
        healthp.x = random.randint(20, 1060)


def weapon_update():
    global wapon
    global prange
    global pspeed
    if wapon == 1:
        weapon.image = "pistol.png"
        prange = 85
        pspeed = 3
    if wapon == 2:
        weapon.image = "ar.png"
        prange = 170
        pspeed = 2
    if wapon == 3:
        weapon.image = "sniper.png"
        prange = 300
        pspeed = 1


def game_update():
    moveplayer()
    banana_move()
    player_check()
    ammo_update()
    ammop_check()
    health_update()
    healthp_update()
    weapon_update()


clock.schedule_interval(game_update, 0.01)
