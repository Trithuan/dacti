import pygame
import sys
import os
from keyboard import finger
from k_event import k_event
from keyboard import stoped
from GameParam import GameParam
from threading import Timer
import random

pygame.init()
screen_width = 600
screen_height = 600
letter_size = screen_width/8
# min_prime = letter_size/speed + 20
WHITE = pygame.Color(255, 255, 255)
BLUE = pygame.Color(109, 209, 222)
BLACK = pygame.Color(0,  0,  0)
RED = pygame.Color(255, 0, 0)
GOLD = pygame.Color(255,215,0)
score = -1
GREEN = pygame.Color(0, 255, 0)
GRAY = pygame.Color(100, 100, 100)

C_MENU = pygame.Color(54, 57, 63)
marge = 20
ThisGame = GameParam(BLACK, WHITE, letter_size, marge)

limit = 300
perfectlimit = 400
deadlimit = 500
delta = 0





bool_a = False
w_x = 500

font = pygame.font.SysFont("Times New Roman, Arial", 50)
TxMenu = font.render("MENU", True, WHITE)
Txspace = font.render("[PRESS ESPACE]", True, WHITE)
size_menu = 100
menu_x = screen_width / 2 - size_menu/2 + ((size_menu - TxMenu.get_rect().width) / 2)
menu_y = (size_menu - TxMenu.get_rect().height) / 2
posMenu = (menu_x, menu_y)
dif =Txspace.get_rect().width - TxMenu.get_rect().width
pospace = (menu_x - dif/2, menu_y + 200)

music = pygame.mixer.music

music.load("Tigra.mp3")
music.set_volume(0.1)
music_start = True
bulleSound = pygame.mixer.Sound("bulle.wav")
whouv = pygame.mixer.Sound("whouv.wav")
soundError = pygame.mixer.Sound("error.wav")
perfSound = pygame.mixer.Sound("perfSound.wav")
bulleSound.set_volume(0.6)
soundError.set_volume(0.04)
perfSound.set_volume(0.5)



w_y = 50
os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (w_x, w_y)
screen = pygame.display.set_mode([screen_width, screen_height])


def clear(color):
    pygame.draw.rect(screen, color, (0, 0, screen_width, screen_height))


def drawlines(height, color):
    pygame.draw.line(screen, color, (0, height), (screen_width, height))

def drawrect(height, large, color):
    pygame.draw.rect(screen, color, (0, height- large/2, screen_width, large))

def falling_letter():
    for letter in ThisGame.lettre_list:
        letter.fall()
        displayletter(letter)
        ThisGame.offlimit(letter , RED,GREEN, GOLD, limit, deadlimit, perfectlimit, perfSound, bulleSound)
        ThisGame.checkmiss(letter, deadlimit)
        if letter.y > screen_height:
            ThisGame.lettre_list.remove(letter)

def displaycol(game):
    for col in game.col:
        pygame.draw.rect(screen, GRAY, (col*letter_size, 0, letter_size, screen_height))


def displayscore():
    txScore = font.render("score : "+str(ThisGame.score), True, WHITE)
    screen.blit(txScore, (10, screen_height - txScore.get_rect().height))


def bg_black():
    bgblaked = Timer(1, ThisGame.black, args = (BLACK,))
    bgblaked.start()


def displaylives():
    rad = 20
    for x in range(ThisGame.life):
        pygame.draw.circle(screen, GREEN, (int(x*rad*3 + 30), int(rad + 20)), rad)
def displayletter(fLetter):
    pygame.draw.rect(screen, fLetter.color, (fLetter.x, fLetter.y, fLetter.width, fLetter.height))
    lettre = font.render(fLetter.key, True, BLACK)
    screen.blit(lettre, (fLetter.x + (fLetter.width - lettre.get_rect().width)/2, fLetter.y + (fLetter.height - lettre.get_rect().height)/2))
    # bolle = font.render(str(fLetter.first), True, BLACK)
    # screen.blit(bolle, (fLetter.x + (fLetter.width - bolle.get_rect().width)/2, fLetter.y + fLetter.height))


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
while not end:
    k_event()
    ThisGame.bgmusic(music, stoped)
    if ThisGame.menu:
        clear(C_MENU)
        if score >= 0:
            txscore = font.render("score : " + str(score), True, WHITE)
            poscore = ((screen_width - txscore.get_rect().width)/2, screen_height/2)
            screen.blit(txscore, poscore)
        screen.blit(TxMenu, posMenu)
        screen.blit(Txspace, pospace)
        if len(stoped) > 0:
            if stoped[0]:
                ThisGame.menu = False
                stoped.remove(True)
    else:
        if not game_over:
            delta += 1
            if ThisGame.miss:
                soundError.play()
                r = random.randint(0, 255)
                v = random.randint(0, 255)
                b = random.randint(0, 255)
                ThisGame.bgcolor = pygame.color.Color(r, v, b)
                ThisGame.life -= 1
                bg_black()
                ThisGame.miss = False
            clear(ThisGame.bgcolor)
            ThisGame.col_light()
            displaycol(ThisGame)
            ThisGame.pop_key(screen_width, screen_height)
            drawlines(limit, RED)
            drawlines(deadlimit, RED)
            displaylives()
            drawrect(perfectlimit, ThisGame.marge, GOLD)
            falling_letter()
            if ThisGame.life <= 0:
                game_over = True
                ThisGame.end = True
            ThisGame.accel(whouv)
            displayscore()
        else:
            score = ThisGame.score
            ThisGame = GameParam(BLACK, WHITE, screen_width/8, 10)
            game_over = False
            stoped.clear()
    clock.tick(60)

    pygame.display.update()
