import pygame
import sys
import os
from keyboard import finger
from k_event import k_event
from keyboard import stoped
from GameParam import GameParam
from settings import *
from affichage import *
import random
from playlist import playlist


def resetmusic():
    zic = random.choice(playlist)
    print('music : ' + zic)
    music.load("music/"+zic)


resetmusic()



def falling_letter(ThisGame):
    for letter in ThisGame.lettre_list:
        letter.fall()
        displayletter(letter)
        ThisGame.offlimit(letter , RED,GREEN, GOLD, limit, deadlimit, perfectlimit, perfSound, bulleSound)
        ThisGame.checkmiss(letter, deadlimit)
        if letter.y > screen_height:
            ThisGame.lettre_list.remove(letter)


ThisGame = GameParam(BLACK, WHITE, letter_size, marge, speed)


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
            if not ThisGame.music_start:
                resetmusic()
                music.play()
                ThisGame.music_start = True
            delta += 1
            if ThisGame.miss:
                soundError.play()
                r = random.randint(0, 255)
                v = random.randint(0, 255)
                b = random.randint(0, 255)
                ThisGame.bgcolor = pygame.color.Color(r, v, b)
                ThisGame.life -= 1
                bg_black(ThisGame)
                ThisGame.miss = False
            clear(ThisGame.bgcolor)
            ThisGame.col_light()
            displaycol(ThisGame)
            ThisGame.pop_key(screen_width, screen_height)
            drawlines(limit, RED)
            drawlines(deadlimit, RED)
            drawrect(perfectlimit, ThisGame.marge, GOLD)
            falling_letter(ThisGame)
            displaylives(ThisGame)
            ThisGame.accel(whouv)
            displayscore(ThisGame)
            if ThisGame.life <= 0:
                game_over = True
                ThisGame.end = True
        else:
            score = ThisGame.score
            ThisGame = GameParam(BLACK, WHITE, screen_width/8, 10, speed)
            game_over = False
            stoped.clear()
    clock.tick(60)

    pygame.display.update()
