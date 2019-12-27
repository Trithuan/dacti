import pygame
import sys
import os
from keyboard import Keyboard
from keyboard import finger
from k_event import k_event
from threading import Timer
from keyboard import stoped
import random

pygame.init()
screen_width = 600
letter_size = screen_width/8
count = 0
score = 0
screen_height = 600
t_count = 0
miss = False
limit = 300
delta = 0
clickable = []
pause = False
speed = 2
min_prime = letter_size/speed + 20
delay_min = min_prime
bool_a = False
w_x = 500
WHITE = pygame.Color(255, 255, 255)
BLUE = pygame.Color(109, 209, 222)
BLACK = pygame.Color(0,  0,  0)
RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)
GRAY = pygame.Color(100, 100, 100)
C_MENU = pygame.Color(54, 57, 63)
key_col = WHITE

font = pygame.font.SysFont("Times New Roman, Arial", 50)
TxMenu = font.render("MENU", True, WHITE)
Txspace = font.render("[PRESS ESPACE]", True, WHITE)
size_menu = 100
menu_x = screen_width / 2 - size_menu/2 + ((size_menu - TxMenu.get_rect().width) / 2)
menu_y = (size_menu - TxMenu.get_rect().height) / 2
posMenu = (menu_x, menu_y)
dif =Txspace.get_rect().width - TxMenu.get_rect().width
pospace = (menu_x - dif/2, menu_y + 200)

pygame.mixer.music.load("Tigra.mp3")
pygame.mixer.music.set_volume(0.1)
bulleSound = pygame.mixer.Sound("bulle.wav")
music_start = True
whouv = pygame.mixer.Sound("whouv.wav")
soundError = pygame.mixer.Sound("error.wav")
bulleSound.set_volume(0.6)
soundError.set_volume(0.04)



w_y = 50
os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (w_x, w_y)
screen = pygame.display.set_mode([screen_width, screen_height])

resetbg = True
def black():
    global c_color
    global resetbg
    c_color = BLACK
    resetbg = True

def bg_black():
    bgblaked = Timer(0.5, black)
    bgblaked.start()


def clear(color):
    pygame.draw.rect(screen, color, (0, 0, screen_width, screen_height))


def redline():
    pygame.draw.line(screen, RED, (0, limit), (screen_width, limit))


class FallingKey:

    def __init__(self, key, col):
        self.key = key
        self.finger = self.finger()
        self.width = screen_width/8
        self.height = screen_height/8
        self.x = self.get_x()
        self.y = 0
        self.speed = speed
        self.color = col
        self.primeColor = WHITE
        self.mustclick = False
        self.clicked = False
        self.clickable = False

    def fall(self):
        self.y += self.speed

    def display(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        lettre = font.render(self.key, True, BLACK)
        screen.blit(lettre, (self.x + (self.width - lettre.get_rect().width)/2, self.y + (self.height - lettre.get_rect().height)/2))

    def offlimit(self, color):
        # TODO: validation animation disparaitre rapide
        # TODO: marge d'erreur et perfect timing
        global clickable

        if limit - self.height < self.y < limit:
            self.color = color
            self.mustclick = True
            self.checkclick()
            if not self.clickable:
                clickable.append(self)
                self.clickable = True
        else:
            self.mustclick = False
            for x in clickable:
                if x == self:
                    clickable.remove(self)

    def get_x(self):
        return self.finger * self.width

    def checkmiss(self):
        global count
        global miss
        if self.y > limit + 20 and not self.clicked:
            count += 1
            # print(count,"t'es nul")
            miss = True

    def finger(self):
        for sub in finger:
            for i in sub:
                if i == self.key:
                    return finger.index(sub)

    def checkclick(self):
        global delta
        global score
        if self.mustclick and Keyboard[self.key]:
            # self.color = GREEN
            if not self.clicked:
                bulleSound.play()
                score += 1
                # print(delta)
            self.clicked = True
            delta = 0

switch = True

def blink():
    global key_col
    global switch
    global lettre_list
    if switch:
        key_col = BLUE
        switch = False
    else:
        key_col = WHITE
        switch = True
    # for letter in lettre_list:
    #     letter.color = pygame.color.Color(red, green, blue)

def accel():
    global t_count
    global speed
    global min_prime
    t_count += 1
    if t_count > 1200:
        whouv.play()
        blink()
        speed += 0.2
        min_prime = letter_size/speed + 20
        t_count = 0


lettre_list = []


def falling_letter():
    for letter in lettre_list:
        letter.fall()
        letter.display()
        if letter.clicked:
            letter.offlimit(GREEN)
        else:
            letter.offlimit(RED)
        letter.checkmiss()
        if letter.y > screen_height:
            lettre_list.remove(letter)


def displayscore():
    txScore = font.render("score : "+str(score), True, WHITE)
    screen.blit(txScore, (txScore.get_rect().height, screen_height - txScore.get_rect().height))


def bgmusic():
    global music_start
    global pause
    if music_start:
        pygame.mixer.music.play(0)
        music_start = False
    elif len(stoped):
        if stoped[0] and not menu:
            pygame.mixer.music.fadeout(1000)


def pop_key(liste):
    # TODO: mot aparrait prédéfinis comme partition
    # TODO: charger partition depuis mémoire
    # TODO: enlever les globaux
    delay = random.random()
    global delay_min
    if len(liste) < 20 and delay < 0.1 and delay_min < 0:
        # alpha = random.choice(keys)
        index_finger = random.randint(0, 7)
        index_letter = random.randint(0, len(finger[index_finger]) - 1)
        alpha = finger[index_finger][index_letter]
        buf_lettre = FallingKey(alpha, key_col)

        liste.append(buf_lettre)
        delay_min = min_prime
    else:
        delay_min -= 1


def get_finger(a):
    for x in range(len(finger)):
        for y in range(len(finger[x])):
            if finger[x][y] == a:
                return x
    return -1


def col_light():
    global miss
    for alpha in Keyboard:
        wellclicked = False
        if Keyboard[alpha]:
            for letter in clickable:
                if letter.key == alpha:
                    wellclicked = True
                    break
                else:
                    wellclicked = False
            if not wellclicked:
                miss = True
            col = get_finger(alpha)
            pygame.draw.rect(screen, GRAY, (col*letter_size, 0, letter_size, screen_height))


clock = pygame.time.Clock()
end = False
c_color = BLACK
# TODO: musique syncro / sur bouton
# TODO: 3 vies et croix en bg à chaque erreur
# TODO: button speed / level
# TODO: last char pressed
# TODO: juicy effect
# TODO: affichage séparation gauche droite
# TODO: mode piano
game_over = False
menu = True
while not end:
    k_event()
    bgmusic()
    if menu:
        clear(C_MENU)
        screen.blit(TxMenu, posMenu)
        screen.blit(Txspace, pospace)
        if len(stoped) > 0:
            if stoped[0]:
                menu = False
                stoped.remove(True)
    elif not game_over:
        delta += 1
        if miss:
            soundError.play()
            r = random.randint(0, 255)
            v = random.randint(0, 255)
            b = random.randint(0, 255)
            c_color = pygame.color.Color(r, v, b)
            bg_black()
            miss = False
        clear(c_color)
        col_light()
        pop_key(lettre_list)
        falling_letter()
        redline()
        accel()
        displayscore()
    clock.tick(60)

    pygame.display.update()
