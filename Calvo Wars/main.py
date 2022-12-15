import os.path

import pygame
import random
from pygame.locals import *
from sys import exit
from PPlay.window import *
from PPlay.keyboard import *
from PPlay.sprite import *
from PPlay.gameobject import *
from PPlay.collision import *
from PPlay.gameimage import *

pygame.init()
pygame.font.init()

clock = pygame.time.Clock()
FPS = 120

# Window Settings
win_width = 1200
win_height = 700
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption('Calvo Wars ')
scroll = 0

# Load and Size Images
background = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join("Sprites", "Background", "background.png")), (win_width, win_height)), 360)
gameover = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join("Sprites", "Background", "gameover.png")), (win_width, win_height)), 360)
menu = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join("Sprites", "Background", "menu.jpg")), (win_width, win_height)), 360)
spaceshipImg = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join("Sprites", "Spaceship", "spaceship.png")), (30, 40)), 270)
enemyImg = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join("Sprites", "Enemy", "enemy.png")), (30, 40)), 90)
bulletImg = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join("Sprites", "Bullet", "bullet.png")), (60, 60)), 180)
enemybulletImg = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join("Sprites", "Bullet", "enemy_bullet.png")), (60, 40)), 180)
bossbulletImg = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join("Sprites", "CalvoBoss", "bullet.png")), (100, 65)), 180)
vidaImg = pygame.transform.scale(pygame.image.load(os.path.join("Sprites", "CalvoHero", "vida.png")), (40, 40))
bonusImg = pygame.transform.scale(pygame.image.load(os.path.join("Sprites", "Bonus", "heart.png")), (140, 100))

# Calvo Sprites
escalax = 150
escalay = 150
anda = [pygame.transform.scale(pygame.image.load(os.path.join("Sprites", "CalvoHero", "parado1.png")), (escalax, escalay)),
        pygame.transform.scale(pygame.image.load(os.path.join("Sprites", "CalvoHero", "anda1.png")), (escalax, escalay)),
        pygame.transform.scale(pygame.image.load(os.path.join("Sprites", "CalvoHero", "anda2.png")), (escalax, escalay)),
        pygame.transform.scale(pygame.image.load(os.path.join("Sprites", "CalvoHero", "anda3.png")), (escalax, escalay)),
        pygame.transform.scale(pygame.image.load(os.path.join("Sprites", "CalvoHero", "anda4.png")), (escalax, escalay)),
        pygame.transform.scale(pygame.image.load(os.path.join("Sprites", "CalvoHero", "anda5.png")), (escalax, escalay)),
        pygame.transform.scale(pygame.image.load(os.path.join("Sprites", "CalvoHero", "anda6.png")), (escalax, escalay)),
        pygame.transform.scale(pygame.image.load(os.path.join("Sprites", "CalvoHero", "anda7.png")), (escalax, escalay)),
        ]

# Calvo Atira

atira = [pygame.transform.scale(pygame.image.load(os.path.join("Sprites", "CalvoHero", "atira1.png")), (escalax, escalay)),
        pygame.transform.scale(pygame.image.load(os.path.join("Sprites", "CalvoHero", "atira2.png")), (escalax, escalay)),
        pygame.transform.scale(pygame.image.load(os.path.join("Sprites", "CalvoHero", "atira3.png")), (escalax, escalay)),
        pygame.transform.scale(pygame.image.load(os.path.join("Sprites", "CalvoHero", "atira4.png")), (escalax, escalay)),
        pygame.transform.scale(pygame.image.load(os.path.join("Sprites", "CalvoHero", "atira5.png")), (escalax, escalay)),
        pygame.transform.scale(pygame.image.load(os.path.join("Sprites", "CalvoHero", "atira6.png")), (escalax, escalay)),
        pygame.transform.scale(pygame.image.load(os.path.join("Sprites", "CalvoHero", "atira7.png")), (escalax, escalay)),
        pygame.transform.scale(pygame.image.load(os.path.join("Sprites", "CalvoHero", "atira8.png")), (escalax, escalay)),
        pygame.transform.scale(pygame.image.load(os.path.join("Sprites", "CalvoHero", "atira9.png")), (escalax, escalay)),
        pygame.transform.scale(pygame.image.load(os.path.join("Sprites", "CalvoHero", "atira10.png")), (escalax, escalay)),
        ]
morreu = [None]*7
for picIndex in range(1, 7):
    morreu[picIndex-1] = pygame.transform.scale(pygame.image.load(os.path.join("Sprites", "CalvoHero", "morreu" + str(picIndex) + ".png")), (2.5*escalax, 2.5*escalay))

# Calvo Enemy Sprites

anda_enemy = [None]*9
for picIndex in range(1, 9):
    anda_enemy[picIndex-1] = pygame.transform.scale(pygame.image.load(os.path.join("Sprites", "CalvoEnemy", "anda" + str(picIndex) + ".png")), (escalax, escalay))

atira_enemy = [pygame.transform.scale(pygame.image.load(os.path.join("Sprites", "CalvoEnemy", "atira1.png")), (escalax, escalay)),
                pygame.transform.scale(pygame.image.load(os.path.join("Sprites", "CalvoEnemy", "atira2.png")), (escalax, escalay)),
                pygame.transform.scale(pygame.image.load(os.path.join("Sprites", "CalvoEnemy", "atira3.png")), (escalax, escalay)),
                pygame.transform.scale(pygame.image.load(os.path.join("Sprites", "CalvoEnemy", "atira4.png")), (escalax, escalay)),
                pygame.transform.scale(pygame.image.load(os.path.join("Sprites", "CalvoEnemy", "atira5.png")), (escalax, escalay)),
                pygame.transform.scale(pygame.image.load(os.path.join("Sprites", "CalvoEnemy", "atira6.png")), (escalax, escalay)),
                ]

# Calvo Enemy Boss
anda_boss = [None]*9
for picIndex in range(1, 9):
    anda_boss [picIndex-1] = pygame.transform.scale(pygame.image.load(os.path.join("Sprites", "CalvoBoss", "anda" + str(picIndex) + ".png")), (1.45*escalax, 1.45*escalay))

atira_boss = [pygame.transform.scale(pygame.image.load(os.path.join("Sprites", "CalvoBoss", "atira1.png")), (1.45*escalax, 1.45*escalay)),
                pygame.transform.scale(pygame.image.load(os.path.join("Sprites", "CalvoBoss", "atira2.png")), (1.45*escalax, 1.45*escalay)),
                pygame.transform.scale(pygame.image.load(os.path.join("Sprites", "CalvoBoss", "atira3.png")), (1.45*escalax, 1.45*escalay)),
                pygame.transform.scale(pygame.image.load(os.path.join("Sprites", "CalvoBoss", "atira4.png")), (1.45*escalax, 1.45*escalay)),
                pygame.transform.scale(pygame.image.load(os.path.join("Sprites", "CalvoBoss", "atira5.png")), (1.45*escalax, 1.45*escalay)),
                pygame.transform.scale(pygame.image.load(os.path.join("Sprites", "CalvoBoss", "atira6.png")), (1.45*escalax, 1.45*escalay)),
                ]

hit_boss = [pygame.transform.scale(pygame.image.load(os.path.join("Sprites", "CalvoBoss", "hit1.png")), (1.45*escalax, 1.45*escalay)),
                pygame.transform.scale(pygame.image.load(os.path.join("Sprites", "CalvoBoss", "hit2.png")), (1.45*escalax, 1.45*escalay)),
                pygame.transform.scale(pygame.image.load(os.path.join("Sprites", "CalvoBoss", "hit3.png")), (1.45*escalax, 1.45*escalay)),
                pygame.transform.scale(pygame.image.load(os.path.join("Sprites", "CalvoBoss", "hit4.png")), (1.45*escalax, 1.45*escalay)),
                pygame.transform.scale(pygame.image.load(os.path.join("Sprites", "CalvoBoss", "hit5.png")), (1.45*escalax, 1.45*escalay)),
                pygame.transform.scale(pygame.image.load(os.path.join("Sprites", "CalvoBoss", "hit6.png")), (1.45*escalax, 1.45*escalay)),
                ]

# Classes
class Spaceship:
    def __init__(self, x, y):
        # Move
        self.x = x
        self.y = y
        self.velx = 7
        self.vely = 7
        self.stepIndex = 0
        self.shotIndex = 0
        self.atira_value = False

        # Level
        self.lvl = 1
        self.lvl_upgrade = 0
        self.lvl_speed = 0

        # Vida
        self.vida = 5
        self.coracoes = []
        self.vidaX = 50

        # Bullet
        self.bullets = []
        self.cool_down_count = 0
        self.cool_down_limit = 30

        # Score
        self.score = 0

        # Hitbox
        self.hitbox = (self.x, self.y, 64, 64)

    def nivel(self):
        if(self.lvl_upgrade >= 500):
            self.lvl += 1
            self.velx += 0.5
            self.cool_down_limit -= 1
            self.lvl_upgrade = 0

    def move_spaceship(self, userInput):
        if userInput[pygame.K_RIGHT]:
            if self.x < 1150:
                self.x += self.velx
        if userInput[pygame.K_LEFT]:
            if self.x > 20:
                self.x -= self.velx
        if userInput[pygame.K_UP]:
            if self.y > 20:
                self.y -= self.vely
        if userInput[pygame.K_DOWN]:
            if self.y < 550:
               self.y += self.vely

    def draw(self, win):
        #win.blit(spaceshipImg, (self.x, self.y))
        if self.atira_value == False:
            if self.stepIndex >= 7:
                self.stepIndex = 0
            win.blit(anda[self.stepIndex], (self.x, self.y))
            self.stepIndex+=1
        else:
            if self.shotIndex < 10:
                win.blit(atira[self.shotIndex], (self.x, self.y))
                self.shotIndex+=1
            else:
                self.shotIndex = 0
                self.atira_value = False

        self.hitbox = (self.x, self.y, 100, 100)

    def cooldown(self):
        if self.cool_down_count >= self.cool_down_limit:
            self.cool_down_count = 0
        elif self.cool_down_count > 0:
            self.cool_down_count += 1

    def shoot(self):
        self.hit()
        self.cooldown()
        if (userInput[pygame.K_SPACE] and self.cool_down_count == 0):
            self.atira_value = True
            bullet = Bullet(self.x, self.y + 40, 1)
            self.bullets.append(bullet)
            self.cool_down_count = 1
        for bullet in self.bullets:
            bullet.move()
            if bullet.off_screen():
                self.bullets.remove(bullet)

    def show_vida(self):
        while len(self.coracoes) != self.vida:
            coracao = Vida(self.vidaX)
            self.coracoes.append(coracao)
            self.vidaX += 50

    def hit(self):
        for enemy in enemies:
            for bullet in self.bullets:
                if enemy.hitbox[0] < bullet.x < enemy.hitbox[0] + enemy.hitbox[2] and enemy.hitbox[1] < bullet.y < enemy.hitbox[1] + enemy.hitbox[3]:
                    self.score += 33
                    self.lvl_upgrade += 33
                    enemies.remove(enemy)
                    self.bullets.remove(bullet)
        for bonus in bonushearts:
            for bullet in self.bullets:
                if bonus.hitbox[0] < bullet.x < bonus.hitbox[0] + bonus.hitbox[2] and bonus.hitbox[1] < bullet.y <  bonus.hitbox[1] + bonus.hitbox[3]:
                    self.score += 5
                    self.lvl_upgrade += 5
                    bonushearts.remove(bonus)
                    self.bullets.remove(bullet)
                    self.vida += 1
        for boss in boss_enemies:
            for bullet in self.bullets:
                if boss.hitbox[0] < bullet.x < boss.hitbox[0] + boss.hitbox[2] and boss.hitbox[1] < bullet.y < boss.hitbox[1] + boss.hitbox[3]:
                    boss.vida -= 1
                    boss.hit_value = True
                    if boss.vida == 0:
                        self.score += 55
                        self.lvl_upgrade += 55
                        boss_enemies.remove(boss)
                    self.bullets.remove(bullet)

class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        # Speed
        self.velx = random.randrange(3, 7)
        self.vely = 7

        # Bullet
        self.bullets = []
        self.cool_down_count = 0
        self.cool_down_limit = random.randrange(50, 150)
        self.atira_value = False

        # Hitbox
        self.hitbox = (self.x, self.y, 64, 64)

        # Sprite
        self.stepIndex = 0
        self.shotIndex = 0

    def draw(self, win):
        if self.atira_value == False:
            if self.stepIndex >= 8:
                self.stepIndex = 0
            win.blit(anda_enemy[self.stepIndex], (self.x, self.y))
            self.stepIndex+=1
        else:
            if self.shotIndex < 6:
                win.blit(atira_enemy[self.shotIndex], (self.x, self.y))
                self.shotIndex+=1
            else:
                self.shotIndex = 0
                self.atira_value = False

        self.hitbox = (self.x, self.y, 100, 100)

    def move_space_ship(self):
        self.x -= self.velx

    def cooldown(self):
        if self.cool_down_count >= self.cool_down_limit:
            self.cool_down_count = 0
        elif self.cool_down_count > 0:
            self.cool_down_count += 1

    def shoot(self):
        self.hit()
        self.cooldown()
        if(self.cool_down_count == 0):
            self.atira_value = True
            bullet = Bullet(self.x, self.y+40, -1)
            self.bullets.append(bullet)
            self.cool_down_count = 1

        for bullet in self.bullets:
            bullet.move()
            if bullet.off_screen():
                self.bullets.remove(bullet)

    def hit(self):
        for bullet in self.bullets:
            if player.hitbox[0] < bullet.x < player.hitbox[0] + player.hitbox[2] and player.hitbox[1] < bullet.y < player.hitbox[1] + player.hitbox[3]:
                player.vida -= 1
                player.vidaX -= 50
                player.coracoes.pop()
                self.bullets.remove(bullet)

    def off_screen(self):
        return not(self.x >= 0)

class BossCalvo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        # Speed
        self.velx = 0.5

        # Vida
        self.vida = 3

        # Bullet
        self.bullets = []
        self.cool_down_count = 0
        self.cool_down_limit = 200
        self.atira_value = False
        self.hit_value = False

        # Hitbox
        self.hitbox = (self.x, self.y, 64, 150)

        # Sprite
        self.stepIndex = 0
        self.shotIndex = 0

    def draw(self, win):
        if self.atira_value == False and self.hit_value == False:
            if self.stepIndex >= 8:
                self.stepIndex = 0
            win.blit(anda_boss[self.stepIndex], (self.x, self.y))
            self.stepIndex += 1
        elif self.hit_value == False:
            if self.shotIndex < 6:
                win.blit(atira_boss[self.shotIndex], (self.x, self.y))
                self.shotIndex += 1
            else:
                self.shotIndex = 0
                self.atira_value = False
        else:
            self.y -= 10
            if self.shotIndex < 6:
                win.blit(hit_boss[self.shotIndex], (self.x, self.y))
                self.shotIndex += 1
            else:
                self.shotIndex = 0
                self.hit_value = False
            self.y += 10

        self.hitbox = (self.x, self.y+40, 100, 150)

    def move_space_ship(self):
        self.x -= self.velx

    def cooldown(self):
        if self.cool_down_count >= self.cool_down_limit:
            self.cool_down_count = 0
        elif self.cool_down_count > 0:
            self.cool_down_count += 1

    def shoot(self):
        self.hit()
        self.cooldown()
        if(self.cool_down_count == 0 and self.x < win.get_width() + 100):
            self.atira_value = True
            bullet = Bullet(self.x, self.y+40, -0.5)
            self.bullets.append(bullet)
            self.cool_down_count = 1

        for bullet in self.bullets:
            bullet.move()
            if bullet.off_screen():
                self.bullets.remove(bullet)

    def hit(self):
        for bullet in self.bullets:
            if player.hitbox[0] < bullet.x < player.hitbox[0] + player.hitbox[2] and player.hitbox[1] < bullet.y < player.hitbox[1] + player.hitbox[3]:
                if player.vida >= 3:
                    player.vida -= 3
                    player.vidaX -= 150
                    player.coracoes.pop()
                    player.coracoes.pop()
                    player.coracoes.pop()
                    self.bullets.remove(bullet)
                else:
                    while len(player.coracoes) != 0:
                        player.vida -= 1
                        player.vidaX -= 50
                        player.coracoes.pop()
                    self.bullets.remove(bullet)

    def off_screen(self):
        return not(self.x >= 0)


class Vida:
    def __init__(self, x):
        self.x = x
        self.y = 35

    def draw_vida(self):
        win.blit(vidaImg, (self.x, self.y))

class BonusHeart:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 2
        self.hitbox = (self.x, self.y, 64, 64)

    def move(self):
        self.x -= self.vel

    def draw_heart(self):
        win.blit(bonusImg, (self.x, self.y))
        self.hitbox = (self.x, self.y, 64, 64)

    def off_screen(self):
        return not (self.x >= 0)

class Bullet:
    def __init__(self, x, y, direcao):
        self.x = x + 8
        self.y = y + 5
        self.direcao = direcao

    def draw_bullet(self):
        if self.direcao == 1:
            win.blit(bulletImg, (self.x, self.y))
        elif self.direcao == -1:
            win.blit(enemybulletImg, (self.x, self.y))
        else:
            win.blit(bossbulletImg, (self.x, self.y))

    def move(self):
        self.x += 15 * self.direcao

    def off_screen(self):
        return not(self.x >= 0 and self.x <= win_width)


# Draw Game
def draw_game(scroll):
    win.fill((0, 0, 0))
    for i in range(0, 2):
        win.blit(background, (i*background.get_width() + scroll, 0))

    player.draw(win)

    for enemy in enemies:
        enemy.draw(win)

    for boss in boss_enemies:
        boss.draw(win)

    for bullet in player.bullets:
        bullet.draw_bullet()

    for enemy in enemies:
        for bullet in enemy.bullets:
            bullet.draw_bullet()

    for boss in boss_enemies:
        for bullet in boss.bullets:
            bullet.draw_bullet()

    for coracao in player.coracoes:
        coracao.draw_vida()

    for bonus in bonushearts:
        bonus.draw_heart()

    level = font.render("Lvl: " + str(player.lvl), True, (255, 255, 255))
    win.blit(level, (player.x + 55, player.y + 15))

    score = scoreFont.render("Score: " + str(player.score), True, (255, 255, 255))
    win.blit(score, (win_width-150, 35))

    pygame.time.delay(15)
    pygame.display.update()
    clock.tick(FPS)

# Defining Player and Enemies
player = Spaceship(250, 500)
enemies = []
boss_enemies = []
bonushearts = []

# Score
font = pygame.font.SysFont('freesansbold', 24)
scoreFont = pygame.font.SysFont('freesansbold', 30)
calvouFont = pygame.font.SysFont('freesansbold', 200)

def increase_scroll(scroll):
    scroll -= 5
    if abs(scroll) > win_width:
        scroll = 0

    return scroll

def GameOver(scroll):
    stepIndex = 0
    cool_down = 0
    cool_down_limit = 30
    exit = False
    pygame.mixer.music.play(-1)

    while not exit:

        for event in pygame.event.get():

            # Quit Game
            if event.type == QUIT:
                pygame.quit()
                exit()

        userInput = pygame.key.get_pressed()

        win.fill((0, 0, 0))
        #win.blit(gameover, (0, 0))
        for i in range(0, 2):
            win.blit(gameover, (i * gameover.get_width() + scroll, 0))

        calvou = calvouFont.render("CALVOU", True, (255, 255, 255))
        win.blit(calvou, (300, 150))

        level = font.render("Lvl: " + str(player.lvl), True, (255, 255, 255))
        win.blit(level, (550, 350))

        score = scoreFont.render("Score: " + str(player.score), True, (255, 255, 255))
        win.blit(score, (530, 300))

        scroll = increase_scroll(scroll)

        if stepIndex >= 5:
            stepIndex = 0

        if cool_down == 0:
            stepIndex += 1
            cool_down += 1
        else:
            cool_down += 1
            if cool_down == cool_down_limit:
                cool_down = 0

        win.blit(morreu[stepIndex], (370, 300))

        if userInput[pygame.K_SPACE]:
            exit = True
            pygame.mixer.music.stop()
            musica_over = pygame.mixer.music.load('Prepare.wav')

        pygame.time.delay(15)
        pygame.display.update()
        clock.tick(FPS)

indiceMenu = 1
def Menu(scroll):
    exit = False
    stepIndex = 0
    cool_down = 0
    cool_down_limit = 5
    stepIndex = 0
    musica_menu = pygame.mixer.music.load('Title.wav')
    pygame.mixer.music.play(-1)

    while not exit:

        for event in pygame.event.get():

            # Quit Game
            if event.type == QUIT:
                pygame.quit()
                exit()

        userInput = pygame.key.get_pressed()
        win.fill((0, 0, 0))

        for i in range(0, 2):
            win.blit(menu, (i * menu.get_width() + scroll, 0))

        if stepIndex >= 7:
            stepIndex = 0

        if cool_down == 0:
            stepIndex += 1
            cool_down += 1
        else:
            cool_down += 1
            if cool_down == cool_down_limit:
                cool_down = 0

        calvou = calvouFont.render("CALVO", True, (255, 255, 255))
        legend = calvouFont.render("WARS", True, (255, 255, 255))
        start = scoreFont.render("Pressione espaço para começar...", True, (255, 255, 255))
        win.blit(start, (650, 375))
        win.blit(calvou, (550, 150))
        win.blit(legend, (598, 250))

        scroll = increase_scroll(scroll)

        win.blit(pygame.transform.scale(anda[stepIndex], (600, 600)), (75, 70))

        if userInput[pygame.K_SPACE]:
            exit = True
            pygame.mixer.music.stop()
            musica_game = pygame.mixer.music.load('Prepare.wav')

        pygame.time.delay(15)
        pygame.display.update()
        clock.tick(FPS)

musicatoca = 0
# Mainloop
while True:

    if(indiceMenu == 1):
        Menu(scroll)
        indiceMenu = 0

    if musicatoca == 0:
        pygame.mixer.music.play(-1)
        musicatoca = 1

    for event in pygame.event.get():

        # Quit Game
        if event.type == QUIT:
            pygame.quit()
            exit()

    # Input
    userInput = pygame.key.get_pressed()

    # Movement
    player.move_spaceship(userInput)

    # Enemy
    while len(enemies) < 3:
        enemy = Enemy(random.randrange(win_width, win_width+100), random.randrange(10, win_height-200))
        enemies.append(enemy)
    for enemy in enemies:
        if enemy.off_screen():
            player.vida -= 1
            player.coracoes.pop()
            player.vidaX -= 50
            enemies.remove(enemy)
        else:
            enemy.move_space_ship()
        enemy.shoot()

    # Enemy Boss
    if(random.randrange(1, 300) == 5 and len(boss_enemies) < 1):
        boss = BossCalvo(random.randrange(win_width, win_width+100), random.randrange(10, win_height-200))
        boss_enemies.append(boss)

    for boss in boss_enemies:
        if boss.off_screen():
            while len(player.coracoes) != 0:
                player.vida -= 1
                player.vidaX -= 50
                player.coracoes.pop()
            boss_enemies.remove(boss)
        else:
            boss.move_space_ship()
        boss.shoot()

    # Scroll Background
    scroll = increase_scroll(scroll)

    # Shoot
    player.shoot()

    # Vida
    player.show_vida()

    # Nivel
    if player.lvl <= 5:
        player.nivel()

    # Vida Bonus
    if(random.randrange(1, 500) == 5 and len(bonushearts) < 1):
        bonus = BonusHeart(random.randrange(win_width, win_width+100), random.randrange(10, win_height-200))
        bonushearts.append(bonus)
    for bonus in bonushearts:
        if bonus.off_screen():
            bonushearts.remove(bonus)
        else:
            bonus.move()

    # GAME OVER
    if(player.vida == 0):
        pygame.mixer.music.stop()
        musica_over = pygame.mixer.music.load('Mysterious.wav')
        GameOver(scroll)
        # Reset
        player.vida = 5
        player.show_vida()
        player.velx = 7
        player.cool_down_limit = 30
        player.lvl = 1
        player.score = 0
        player.cool_down_count = 0

        for bullet in player.bullets:
            player.bullets.remove(bullet)

        for enemy in enemies:
            for bullet in enemy.bullets:
                enemy.bullets.remove(bullet)
            enemy.x = random.randrange(win_width, win_width+100)
            enemy.y = random.randrange(10, win_height-200)

        for boss in boss_enemies:
            for bullet in boss.bullets:
                boss.bullets.remove(bullet)
            boss.x = random.randrange(win_width, win_width + 100)
            boss.y = random.randrange(10, win_height - 200)

        for heart in bonushearts:
            bonushearts.remove(heart)
        musicatoca = 0

    # Draw Game in Window
    draw_game(scroll)


